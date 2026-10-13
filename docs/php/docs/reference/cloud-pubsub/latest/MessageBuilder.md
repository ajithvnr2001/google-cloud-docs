---
url: https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/MessageBuilder/
title: Cloud PubSub Client - Class MessageBuilder (2.22.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:44.930935+00:00
---

# Cloud PubSub Client - Class MessageBuilder (2.22.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/MessageBuilder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud PubSub Client - Class MessageBuilder (2.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.1 (latest)  2.19.4  2.18.0  2.17.0  2.16.2  2.15.1  2.14.0  2.13.2  2.12.0  2.11.3  2.10.1  2.9.1  2.8.2  2.7.0  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.2  1.50.0  1.49.0  1.48.0  1.47.0  1.46.5  1.45.2  1.44.0  1.43.2  1.42.1  1.41.3  1.40.1  1.39.3 

Reference documentation and code samples for the Cloud PubSub Client class MessageBuilder.

Builds a PubSub Message.

This class may be used to build an API-compliant message for publication.

This class is immutable and each build method returns a new instance with your changes applied.

Note that messages are invalid unless they include a data field or at least one attribute. Both may be provided, but omission of both will result in an error.

Example:
    
    
    use Google\Cloud\PubSub\MessageBuilder;
    use Google\Cloud\PubSub\PubSubClient;
    
    $client = new PubSubClient();
    $topic = $client->topic($topicId);
    
    $builder = new MessageBuilder();
    $builder = $builder->setData('hello friend!')
        ->addAttribute('from', 'Bob')
        ->addAttribute('to', 'Jane');
    
    $topic->publish($builder->build());
    

## Namespace

Google \ Cloud \ PubSub

## Methods 

### __construct

**Parameter**  
---  
**Name** | **Description**  
`message` |  `array`   
The initial message data.  
  
### setData

Set the message data.

Do not base64-encode the value; If it must be encoded, the client will do it on your behalf.

Example:
    
    
    $builder = $builder->setData('Hello friend!');
    

**Parameter**  
---  
**Name** | **Description**  
`data` |  `string`   
The message data field.  
**Returns**  
---  
**Type** | **Description**  
`[MessageBuilder](https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/MessageBuilder)` |   
  
### setAttributes

Set optional attributes for this message.

Example:
    
    
    $builder = $builder->setAttributes([
        'from' => 'Bob'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`attributes` |  `array`   
A set of key/value pairs, where both key and value are strings.  
**Returns**  
---  
**Type** | **Description**  
`[MessageBuilder](https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/MessageBuilder)` |   
  
### addAttribute

Add a single attribute to the message.

Example:
    
    
    $builder = $builder->addAttribute('to', 'Jane');
    

**Parameters**  
---  
**Name** | **Description**  
`key` |  `string`   
The attribute key.  
`value` |  `string`   
The attribute value.  
**Returns**  
---  
**Type** | **Description**  
`[MessageBuilder](https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/MessageBuilder)` |   
  
### setOrderingKey

Set the message's ordering key.

Example:
    
    
    $builder = $builder->setOrderingKey('order');
    

**Parameter**  
---  
**Name** | **Description**  
`orderingKey` |  `string`   
The ordering key.  
**Returns**  
---  
**Type** | **Description**  
`[MessageBuilder](https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/MessageBuilder)` |   
  
### build

Build a message.

Example:
    
    
    $message = $builder->build();
    

**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/Message)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
