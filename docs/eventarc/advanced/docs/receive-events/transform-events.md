---
url: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events/
title: Transform received events \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:32.663108+00:00
---

# Transform received events  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Transform received events Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

You can transform your event data by writing transformation expressions [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel). For example, you can modify event payloads to satisfy a destination's specific API contract.

**Caution:** Don't include sensitive information such as passwords, secrets, or personally identifiable information (PII) in CEL transformation expressions. These expressions are treated as service configuration data by Eventarc Advanced and don't have the same level of [data security](https://cloud.google.com/trust-center/security) as event payloads.

Note that events are always delivered in a [CloudEvents format using an HTTP request in binary content mode](https://docs.cloud.google.com/eventarc/docs/cloudevents) unless you specify a message binding.

## Set the input and output data formats

In addition to writing a transformation expression in CEL, you can optionally specify the data format of the incoming event data. This lets Eventarc Advanced know how to parse the payload of the event. You can also convert the data from one format to another.

The following formats are supported: Avro, JSON, and Protobuf. For more information, see [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events).

**Note:** Before an event format is converted, any transformation that is configured is applied first.

## Transformation expressions

When transforming events, all event attributes can be accessed in a CEL expression as variables through a predefined `message` object. These variables are populated with values based on the event data at runtime. For example:

  * `message.id` returns the `id` attribute of the event
  * `message.data` returns a CEL value representation of the event payload
  * `message.data.some-key` returns the content of a field named `some-key` from the event payload



Fields in `message.data` are always represented as `String` types and values are mapped from the original event using the schema specified when setting the input data format.

The transformation expression should express a complete event that includes the event context attributes and the event data payload. Expressions are written in JSON but predefined CEL functions, macros, and operators, as well as regular expressions using [RE2](https://github.com/google/re2/wiki/Syntax) are supported. Eventarc Advanced also supports certain extension functions that can be used to transform the event data.

The following are two examples of using CEL expressions to transform your event data. For more use cases and examples, see [Transformation examples](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transformation-examples).

#### Example: Format attribute values

The following example formats `phone_number` attribute values using regular expression functions. (Other attributes have been omitted.)
    
    
      // Input:
      // {
      //   "data":
      //   {
      //     "email_address": "charlie@altostrat.com",
      //     "phone_number": "8005550100",
      //   }
      // }
      // Output:
      // {
      //    "data":
      //    {
      //      "email_domain": "altostrat.com",
      //      "phone_number": "(800) 555-0100",
      //      "area_code": "800",
      //      "local_number": "5550100",
      //    }
      // }
    
      {
        "data":
        {
          "email_domain": re.capture(
                            message.data.email_address,
                            "\\S+@(\\S+)"),
    
          "phone_number": re.extract(
                            message.data.phone_number,
                            "^(\\d{3})(\\d{3})(\\d{4})", "(\\1) \\2-\\3"
                          ),
    
        }.merge ( re.captureN(message.data.phone_number,
                            "^(?P\d{3})[\w\-)(]*(?P\d{7})"
                          )
        )
      }

These are the regular expression functions used in the preceding example:

  * `re.capture`: captures the first unnamed or named group value. Arguments are the following: 
    * `target`: string that should be parsed
    * `regex`: regular expression used to capture values

Returns a string of the first captured group value.

  * `re.captureN`: does a full match on the given string and regular expression. Arguments are the following:
    * `target`: string that should be parsed
    * `regex`: regular expression used to capture values

Returns a map with key and value pairs for a named group (group name, captured string) or an unnamed group (group index, captured string).

  * `re.extract`: matches group values from the given target string and rewrites the string. Arguments are the following: 
    * `target`: string that should be parsed
    * `regex`: regular expression used to extract values
    * `rewrite`: regular expression for how the result should be formatted

Returns a string of the extracted values that is formatted based on the `rewrite` argument.




#### Example: Map an array to an array of objects

The following example maps an array of integers into an array of objects. (Other attributes have been omitted.)
    
    
      // Input:
      // {
      //   "data":
      //   {
      //        "product_ids": [1, 2, 3]
      //   }
      // }
      // Output:
      // {
      //    "data":
      //    {
      //             "products": [
      //                {
      //                   "name": "apple",
      //                   "price": 70
      //                },
      //                {
      //                    "name": "orange",
      //                    "price":  80
      //                },
      //                {
      //                    "name": "Product(3)",
      //                    "price": 0
      //                },
      //                {
      //                     "name": "apple",
      //                     "price": 70
      //                }
      //            ]
      //    }
      // }
    
      {
        "data":
        {
          "products":  message.data.product_ids.map(product_id,
                  product_id == 1?
                  {
                    "name": "apple",
                    "price": 70
                  } :
                  product_id == 2?
                  {
                    "name": "orange",
                    "price":  80
                  } :
                  // Default:
                  {
                    "name": "Product(" + string(product_id) + ")",
                    "price": 0
                  }
              )
        }
      }

## Configure a pipeline to transform events

You can configure a pipeline to transform event data in the Google Cloud console or by using the gcloud CLI.

Note that only one mediation per pipeline is supported.

### Console

  1. In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. You can [create a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#console) or, if you are updating a pipeline, click the name of the pipeline.

  3. In the **Pipeline details** page, click edit **Edit**.

  4. In the **Event mediation** pane, do the following:

     1. Select the **Apply a transformation** checkbox.
     2. In the **Inbound format** list, select the applicable format.

For more information, see [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events).

     3. In the **CEL expression** field, write a transformation expression in JSON. Predefined [CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel) functions, macros, and operators, as well as regular expressions are supported. For example:
            
            {
            "id": message.id,
            "datacontenttype": "application/json",
            "data": "{ \"scrubbed\": \"true\" }"
            }

The preceding example does the following:

        * Removes all attributes from the original event except its `id`
        * Sets the `datacontenttype` attribute to `application/json`
        * Replaces the event payload with a static JSON string
     4. Click **Continue**.

  5. In the **Destination** pane, do the following:

     1. If applicable, in the **Outbound format** list, select a format.

For more information, see [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events).

     2. Optionally, apply a **Message binding**. For more information, see the Define a message binding section in this document.

  6. Click **Save**.

It can take a couple of minutes to update a pipeline.




###  gcloud 

  1. Open a terminal.

  2. You can [create a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#gcloud) or you can update a pipeline using the [`gcloud eventarc pipelines update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/update) command:
         
         gcloud eventarc pipelines update PIPELINE_NAME \
             --location=REGION \
             --mediations=transformation_template=\
         '
          {
             TRANSFORMATION_EXPRESSION
          }
         '

**Note:** The `--mediations` flag uses a hash symbol (`#`) as the default delimiter. If your expression contains a hash, specify a different delimiter to avoid parsing conflicts. For more information, see [gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping). For example, to use a semicolon (`;`) as a delimiter:  
`--mediations=^;^transformation_template=TRANSFORMATION_EXPRESSION`

Replace the following:

     * `PIPELINE_NAME`: the ID of the pipeline or a fully qualified name
     * `REGION`: a [supported Eventarc Advanced location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)

Alternatively, you can set the gcloud CLI location property:
           
           gcloud config set eventarc/location REGION
           

     * `TRANSFORMATION_EXPRESSION`: an expression written in JSON. Predefined [CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel) functions, macros, and operators, as well as regular expressions are supported. A `mediations` flag is used to apply a `transformation_template` key.

It can take a couple of minutes to update a pipeline.

Example:
    
    gcloud eventarc pipelines update my-pipeline \
        --location=us-central1 \
        --mediations=transformation_template=\
    '
     {
        "id": message.id,
        "datacontenttype": "application/json",
        "data": "{ \"scrubbed\": \"true\" }"
     }
    '

The preceding example does the following:

     * Removes all attributes from the original event except its `id`
     * Sets the `datacontenttype` attribute to `application/json`
     * Replaces the event payload with a static JSON string



### Extension functions

Eventarc Advanced supports the following extension functions which can be used to transform the event data received through a bus.

Function | Description  
---|---  
`denormalize` | Denormalizes a map or a list by adding redundant data to improve read performance. Field names in the resulting map are delimited using a period (`.`). The list index is converted to a string key, starting from `0`.Note that because you can't use a period (`.`) in Avro and Protobuf field names, only use this function to target JSON data. For example: `map.() -> map(string, dyn)` or `list() -> map(string, dyn)`  
`merge` | Joins two fields and returns the combined field. Fields with duplicate names are merged. For example: `message.(message) -> message`  
`removeFields` | Removes specific fields from an event. Field names are resolved as paths. The period character (`.`) is used as a delimiter. Note that raw JSON is expected. If you marshal the JSON, the transformation might be applied to a JSON string and result in an error. For example: `message.(list(string)) -> message`  
`setField` | Adds or replaces a field of the event with a given key. The field name is resolved as a path. The period character (`.`) is used as a delimiter. For example: `message.(string, dyn) -> message`  
  
#### Example: Add attribute to event payload without modifying other data
    
    
    // Input:
    // {
    //   "data": 
    //   {
    //        "credit_card_number": "XXXX-XXXX-XXXX-XXXX"
    //   }
    // }
    // Output:
    // {
    //    "data":
    //    {
    //        "credit_card_number": "XXXX-XXXX-XXXX-XXXX",
    //        "card_type": "credit"
    //    }
    // }
    {
      "data": message.data.merge(
        {
          "card_type": "credit"
        }
      )
    }

#### Example: Denormalize list of items from event payload
    
    
    // Input:
    //{
    //"data": 
    //   {
    //        "products": [
    //          {
    //            "number": 021774,
    //            "type": "perishable",
    //            "price": 2.00
    //          },
    //          {
    //            "number": 95602,
    //            "type": "diy",
    //            "price": 120.00
    //          },
    //          {
    //            "number": 568302,
    //            "type": "toys",
    //            "price": 12.00
    //          }
    //        ]
    //   }
    //}
    //
    // Output:
    //{
    //"data":
    //    {
    //        "products": {
    //            "0.number": 021774,
    //            "0.type": "perishable",
    //            "0.price": 2.00,
    //            "1.number": 95602,
    //            "1.type": "diy",
    //            "1.price": 120.00,
    //            "2.number": 568302,
    //            "2.type": "toys",
    //            "2.price": 12.00
    //          }
    //   }
    //}
    //
    //
    message.setField("data.products", message.data.products.denormalize())

#### Example: Remove field from event payload
    
    
    // Input:
    // {
    //   "data": 
    //   {
    //     "payment": {
    //       "card_number": "XXXX-XXXX-XXXX-XXXX",
    //       "card_type": "credit",
    //     }
    //   }
    // }
    // Output:
    // {
    //   "data":
    //   {
    //     "payment": {
    //       "card_type": "credit"
    //     }
    //   }
    // }
    message.removeFields(["data.payment.card_number"])

## Define a message binding

By default, events are always delivered to a destination in a [CloudEvents format using an HTTP request in binary content mode](https://docs.cloud.google.com/eventarc/docs/cloudevents). Optionally, you can override this behavior by defining a message binding and constructing a new HTTP request.

Any HTTP headers that are introduced by other policies or controls (for example, OAuth or OIDC tokens) are preserved and merged with the headers resulting from the binding expression.

Note: To execute a Cloud Run job that overrides the job configuration, you must grant the **Cloud Run Developer** (`roles/run.developer`) or **Cloud Run Jobs Executor With Overrides** (`roles/run.jobsExecutorWithOverrides`) IAM role. For more information, see [Override job configuration for a specific execution](https://docs.cloud.google.com/run/docs/execute/jobs#override-job-configuration).

You can define a message binding when configuring a pipeline in the Google Cloud console or by using the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. You can [create a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#console) or, if you are updating a pipeline, click the name of the pipeline.

Note that updating a pipeline might take more than 10 minutes.

  3. In the **Pipeline details** page, click edit **Edit**.

  4. In the **Destination** pane, apply a **Message binding** which is a CEL expression written in JSON. This results in a newly constructed HTTP request which is then sent to the pipeline's destination.

For more information, see the Access inbound messages and Construct HTTP requests sections in this document.

  5. Click **Save**.




###  gcloud 

  1. Open a terminal.

  2. You can [create a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#gcloud) or you can update a pipeline using the [`gcloud eventarc pipelines update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/update) command:
         
         gcloud eventarc pipelines update PIPELINE_NAME \
             --location=REGION \
             --destinations=http_endpoint_message_binding_template='MESSAGE_BINDING'

**Note:** The `--destinations` flag uses a hash symbol (`#`) as the default delimiter. If your expression contains a hash, specify a different delimiter to avoid parsing conflicts. For more information, see [gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping). For example, to use a semicolon (`;`) as a delimiter:  
`--destinations=^;^http_endpoint_message_binding_template='MESSAGE_BINDING'`

Replace the following:

     * `PIPELINE_NAME`: the ID of the pipeline or a fully qualified name
     * `REGION`: a [supported Eventarc Advanced location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)

Alternatively, you can set the gcloud CLI location property:
           
           gcloud config set eventarc/location REGION
           

     * `MESSAGE_BINDING`: a CEL expression written in JSON that results in a newly constructed HTTP request which is then sent to the pipeline's destination.

For more information, see the Access inbound messages and Construct HTTP requests sections in this document.

Example:
    
    gcloud eventarc pipelines create my-pipeline \
        --location=us-central1 \
        --destinations=http_endpoint_uri='https://example-endpoint.com', \
    http_endpoint_message_binding_template='{"headers":{"new-header-key": "new-header-value"}}'

Note that if you are using an `http_endpoint_message_binding_template` key, you must also set the `http_endpoint_uri` key.




### Access inbound messages

You can use a CEL expression to access an inbound CloudEvents message as follows:

  * Use the `message.data` value to access the `data` field of the inbound message.
  * Use the `message.key` values (where `key` is the name of the attribute) to access the attributes of the inbound message.
  * Use a `headers` variable to access any headers added to the HTTP request by previous mediations in the processing chain. This variable defines a map of key-value pairs corresponding to the additional HTTP headers and not to the original headers of the initial inbound request.

For example, the following CEL expression can be used to construct a headers-only HTTP request by adding an additional header to those added in previous pipeline mediations:

`{"headers": headers.merge({"new-header-key": "new-header-value"})}`




### Construct HTTP requests

The result of the CEL expression must be a map of key-value pairs whose `headers` and `body` fields are used to construct the HTTP request as follows.

For `headers` fields:

  * If a `headers` map exists as a result of the CEL expression, its key-value pairs are directly mapped to the HTTP request headers, and its values are constructed using the [canonical string-encoding of the corresponding data type](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#type-system).
  * If a `headers` field doesn't exist, the resulting HTTP request retains any headers added during previous pipeline mediations.



For `body` fields:

  * If a `body` field exists as a result of the CEL expression, its value is directly mapped to the HTTP request body.
  * If the `body` field value is of type `bytes` or `string`, it's used as the HTTP request body as is; otherwise, it's converted to a JSON string.
  * If the `body` field doesn't exist, the resulting HTTP request body is the body of the final CloudEvents HTTP message binding in binary content mode.



Any other fields as a result of the CEL expression are ignored.

### Extension functions

Eventarc Advanced supports the following extension functions which can be used to transform the event data when specifying a message binding.

Function | Description  
---|---  
`merge` | Merges a passed CEL map into the CEL map to which the function is applied. If the same key exists in both maps, or if the key's value is type `map`, both maps are merged; otherwise, the value from the passed map is used. Example: `map1.merge(map2) -> map3`  
`toBase64` | Converts a CEL value to a base64 URL-encoded string. Example: `map.toBase64() -> string`  
`toCloudEventJsonWithPayloadFormat` |  Converts a message to a CEL map that corresponds to a JSON representation of a CloudEvents message, and applies `toDestinationPayloadFormat` to the message data. Also sets the `datacontenttype` of the event to the specified outbound format (`output_payload_format_*`). If an outbound format is not set, any existing `datacontenttype` is used; otherwise, the `datacontenttype` is not set. If the message doesn't adhere to the CloudEvents specification, the function fails. Note that to convert the data to a JSON string, you can use `toJsonString`. Example: ` message.toCloudEventJsonWithPayloadFormat() -> map.toJsonString() -> string`  
`toDestinationPayloadFormat` |  Converts `message.data` to the specified outbound format (`output_payload_format_*`). If an outbound format is not set, `message.data` is returned unchanged. Example: `message.data.toDestinationPayloadFormat() -> string or bytes`  
`toJsonString` | Converts a CEL value to a JSON string. For example: `map.toJsonString() -> string`  
`toMap` | Converts a CEL list of CEL maps to a single CEL map. Example: `list(map).toMap() -> map`  
  
#### Example: Retain headers, add new header, set body to destination format
    
    
    gcloud eventarc pipelines create my-pipeline \
        --location=us-central1 \
        --input-payload-format-json='{}' \
        --destinations=http_endpoint_uri='https://example-endpoint.com',http_endpoint_message_binding_template='{"headers": headers.merge({"content-type":"application/avro"}), "body": message.data.toDestinationPayloadFormat()}',output_payload_format_avro_schema_definition='{"schema_definition": "{"type":"record","name":"myrecord","fields":[{"name":"name","type":"string"},{"name":"account_late","type":"boolean"}]}"}'

## What's next

  * [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events)
  * [Transformation examples](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transformation-examples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
