---
url: https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview/
title: User Defined Functions (UDFs) overview \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:09.086737+00:00
---

# User Defined Functions (UDFs) overview  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  User Defined Functions (UDFs) overview Stay organized with collections  Save and categorize content based on your preferences. 

A JavaScript **User-Defined Function (UDF)** is a type of Single Message Transform (SMT). UDFs provide a flexible way to implement custom transformation logic within Pub/Sub, similar to [BigQuery JavaScript UDFs](https://docs.cloud.google.com/bigquery/docs/user-defined-functions).

UDFs accept a single message as input, perform the defined actions on the input, and return the result of the process.

UDFs have the following key properties:

  * **Code:** The JavaScript code that defines the transformation logic.

  * **Function name:** The name of the JavaScript function within the provided code that Pub/Sub applies to messages.




## Create the JavaScript function

The UDF code must contain a function with the following signature:
    
    
      /**
      * Transforms a Pub/Sub message.
      * @return {(Object<string, (string | Object<string, string>)>|* null)} - To
      * filter a message, return `null`. To transform a message, return a map with
      * the following keys:
      *   - (required) 'data' : {string}
      *   - (optional) 'attributes' : {Object<string, string>}
      * Returning empty `attributes` will remove all attributes from the message.
      *
      * @param  {(Object<string, (string | Object<string, string>)>} - Pub/Sub
      * message. Keys:
      *   - (required) 'data' : {string}
      *   - (required) 'attributes' : {Object<string, string>}
      *
      * @param  {Object<string, any>} metadata - Pub/Sub message metadata.
      * Keys:
      *   - (optional) 'message_id'  : {string}
      *   - (optional) 'publish_time': {string} YYYY-MM-DDTHH:MM:SSZ format
      *   - (optional) 'ordering_key': {string}
      */
      function <function_name>(message, metadata) {
        // Perform custom transformation logic
        return message; // to filter a message instead, return `null`
      }
    

### Inputs

The function takes the following inputs:

  * **`message` argument:** A JavaScript object representing the Pub/Sub message. It contains the following properties:

    * `data`: (`String`, required) The message payload.

    * `attributes`: (`Object<String, String>`, optional) A map of key-value pairs representing message attributes.

  * **`metadata` argument:** A JavaScript object containing immutable metadata about the Pub/Sub message:

    * `message_id`: (`String`, optional) The unique ID of the message.

    * `publish_time`: (`String`, optional) The message's publish time in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format (YYYY-MM-DDTHH:mm:ssZ).

    * `ordering_key`: (`String`, optional) The message's [ordering key](https://docs.cloud.google.com/pubsub/docs/ordering), if applicable.




### Outputs

The function must return one of the following:

  * To transform a message, edit the contents of `message.data` and `message.attributes`, and return the altered `message` object.

  * To filter a message, return `null`.




### Input / Output Requirements

  * If the UDF transforms the message payload, the payload input and output must be UTF-8 encoded strings.
  * If the UDF does not transform the message payload, the payload may use any encoding.
  * Attribute key-value pairs must be UTF-8 encoded strings.



## How UDFs transform a message

The result of running a UDF on a message can be one of the following:

  * The UDF transforms a message.

  * The UDF returns `null`.

    * Topic SMTs: Pub/Sub returns success to the publisher and includes a message ID in the response for the filtered messages. Pub/Sub does not store the message or send it to any subscribers.

    * Subscription SMTs: Pub/Sub acknowledges the message delivery without sending the message to a subscriber.

  * The UDF throws an error.

    * Topic SMTs: Pub/Sub returns the error to the publisher and does not publish any of the messages.

    * Subscription SMTs: Pub/Sub negatively acknowledges the message.




## Create a UDF SMT

SMTs can be configured on Pub/Sub topics or subscriptions.

  * Topic SMTs are executed before Pub/Sub stores the message, and the results are available to all subscribers.
  * Subscription SMTs are executed before the message is delivered, and the results are only available for that subscription.




### Console

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Create either a topic or a subscription.

     * To create a topic, click **Create topic**. The **Create topic** page opens.

     * To create a subscription:

       1. Click the name of the topic where you want the subscription.

       2. Click **Create subscription**. The **Add subscription to topic** page opens.

  3. Under **Transforms** , click **Add a transform**.

  4. For **Transform type** , select **JavaScript UDF**.

  5. Optional: You can use Gemini Enterprise to generate the code for the UDF, as follows:

     1. Click **Generate with AI**.

     2. In the text field, enter a description of what the function should do. For example, "Add a processed_at attribute with the current time".

     3. Click **Submit**. The generated code appears in the **Generate with AI** pane, along with an explanation of the code.

     4. Examine the code for correctness. You might need to refine your description and regenerate the code.

     5. To use the generated code, click **Import**.

  6. In the **Function name** field, enter the name of the JavaScript function that the SMT calls. Example: `redactSSN`.

If you used Gemini Enterprise to generate the code, this field is already filled in.

  7. In the text area, enter the code for the UDF. Example:
         
         function redactSSN(message, metadata) {
           const data = JSON.parse(message.data);
           delete data['ssn'];
           message.data = JSON.stringify(data);
           return message;
         }
         

The code must contain a function whose name matches the **Function name** field.

If you used Gemini Enterprise to generate the code, this field is already filled in.

  8. If you don't want the SMT to be active immediately, select **Disable transform**. When this option is selected, the SMT is created with the topic, but isn't executed on incoming messages. After the topic is created, you can [edit the topic](https://docs.cloud.google.com/pubsub/docs/smts/update-topic-smt) to enable the SMT.

  9. To create the topic or subscription, click **Create**.




###  gcloud 

#### Create a definition file

Create a YAML or JSON file that defines the UDF SMT.

###  YAML 
    
    
    - javascriptUdf:
        code: { FUNCTION_CODE }
        functionName: FUNCTION_NAME
    

###  JSON 
    
    
    {
      "javascriptUdf": {
        "code": {
          FUNCTION_CODE
        }
        "functionName": FUNCTION_NAME
      }
    }
    

Replace the following:

  * FUNCTION_CODE: The Javascript code for the UDF. The code must contain a function whose name matches the `functionName` field. Example:
        
        function redactSSN(message, metadata) {
          const data = JSON.parse(message.data);
          delete data['ssn'];
          message.data = JSON.stringify(data);
          return message;
        }
        

  * FUNCTION_NAME: The name of the JavaScript function that the SMT calls. Example: `redactSSN`.




#### Create a topic or subscription

To create a topic, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command.
    
    
    gcloud pubsub topics create TOPIC_ID \
      --message-transforms-file=TRANSFORMS_FILE
    

Replace the following:

  * TOPIC_ID: The ID or name of the topic you want to create.
  * TRANSFORMS_FILE: The path to the definition file.



To create a subscription, run the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command.
    
    
    gcloud pubsub subscriptions create SUBSCRIPTION_ID \
      --topic=projects/PROJECT_ID/topics/TOPIC_ID \
      --message-transforms-file=TRANSFORMS_FILE
    

Replace the following:

  * SUBSCRIPTION_ID: The ID or name of the subscription to create.

  * PROJECT_ID: The ID of the project that contains the topic.

  * TOPIC_ID: The ID of the topic to subscribe to.

  * TRANSFORMS_FILE: The path to the definition file.




Optionally, you can validate and test the SMT before you create it. For more information, see the following pages:

  * [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt)
  * [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt)



## Limitations

Pub/Sub enforces resource limits on UDFs to ensure efficient transformation operations. The limitations include:

  * A maximum of 20 KB of code per UDF
  * A maximum of 500 ms of execution time per message
  * Support for only [ECMAScript standard built-ins](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)
  * No calls to external APIs
  * No imports of external libraries



## Sample UDFs

Here are some sample UDFs for publishing and subscribing. You can find additional samples in the [UDF library](https://github.com/GoogleCloudPlatform/pubsub/tree/master/udfs).

### Function: Convert a day of the week integer to the corresponding string

When you add the following UDF to a topic or a subscription, the following changes take place during message publish or delivery:

  1. Pub/Sub applies the function to the message. If the message does not have a JSON payload, the UDF throws an error.

  2. The UDF looks for a field called `dayOfWeek` and if the value of this field is a number between 0 and 6, converts it to a corresponding day of the week such as `Monday`. If the field does not exist or the number is not in the range of 0 to 6, the code sets the `dayOfWeek` field to `Unknown`.

  3. The UDF serializes the modified payload back into the message.

  4. Pub/Sub passes the updated message to the next step in your pipeline.



    
    
    function intToString(message, metadata) {
      const data = JSON.parse(message.data);
      switch(`data["dayOfWeek"]`) {
        case 0:
          data["dayOfWeek"] = "Sunday";
          break;
        case 1:
          data["dayOfWeek"] = "Monday";
          break;
        case 2:
          data["dayOfWeek"] = "Tuesday";
          break;
        case 3:
          data["dayOfWeek"] = "Wednesday";
          break;
        case 4:
          data["dayOfWeek"] = "Thursday";
          break;
        case 5:
          data["dayOfWeek"] = "Friday";
          break;
        case 6:
          data["dayOfWeek"] = "Saturday";
          break;
        default:
          data["dayOfWeek"] = "Unknown";
      }
      message.data = JSON.stringify(data);
      return message;
    }
    

### Function: Redact a social security number

When you add the following UDF to a topic or a subscription, the following changes take place during message publish or delivery:

  1. Pub/Sub applies the function to the message. If the message does not have a JSON payload, the UDF throws an error.

  2. The UDF removes the field `ssn` from the message payload (if it exists).

  3. The UDF serializes the modified payload back into the message.

  4. Pub/Sub passes the updated message to the next step in your pipeline.



    
    
    function redactSSN(message, metadata) {
      const data = JSON.parse(message.data);
      delete data['ssn'];
      message.data = JSON.stringify(data);
      return message;
    }
    

### Function: Filter out and auto-ack specific messages

When you add the following UDF to a topic or a subscription, the following changes take place during message publish or delivery:

  1. Pub/Sub applies the function to the message. If the message does not have a JSON payload, the UDF throws an error.

  2. The UDF checks if the payload contains a field called `region`.

  3. If the value of the `region` field is not `US`, the function returns null, causing Pub/Sub to filter the message.

  4. If the value of the `region` field is `US`, Pub/Sub passes the original message to the next step in your pipeline.



    
    
    function filterForUSRegion(message, metadata) {
      const data = JSON.parse(message.data);
      if (data["region"] !== "US") {
        return null;
      }
      return message;
    }
    

### Function: Validate message content to ensure the amount is not greater than 100

When you add the following UDF to a topic or a subscription, the following changes take place during message publish or delivery:

  1. Pub/Sub applies the function to the message. If the message does not have a JSON payload, the UDF throws an error.

  2. The UDF checks if the message contains a field called `amount`.

  3. If the value of the `amount` field is greater than `100`, the function throws an error.

  4. If the value of the `amount` field is not greater than `100`, the function returns the original message.

  5. Pub/Sub then either marks the message as failed, or passes the original message to the next step in your pipeline.



    
    
    function validateAmount(message, metadata) {
      const data = JSON.parse(message.data);
      if (data["amount"] > 100) {
        throw new Error("Amount is invalid");
      }
      return message;
    }
    

## What's next

  * [Choose between topic and subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smts/choose-smts)

  * [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt)

  * [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt)

  * Explore additional samples in the [UDF library](https://github.com/GoogleCloudPlatform/pubsub/tree/master/udfs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
