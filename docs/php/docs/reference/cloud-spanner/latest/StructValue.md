---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/StructValue/
title: Cloud Spanner Client - Class StructValue (2.11.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:53.272450+00:00
---

# Cloud Spanner Client - Class StructValue (2.11.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/StructValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner Client - Class StructValue (2.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner Client class StructValue.

Defines a struct parameter value with its fields.

This class is included to provide a fluent interface to build complex struct parameter values for your queries against Cloud Spanner. If your struct does or may include unnamed fields, or duplicate field names, you must use a StructValue. In most cases, however, an associative array may be used.

Please note that query results expressed as structs will not be returned using this class. Query results will always be expressed as a PHP array. This class is intended to be used to create complex struct values only.

If your query contains duplicate field names, it must be returned as a name/value pair as demonstrated in the example below using `Result::RETURN_NAME_VALUE_PAIR`.

Example:
    
    
    use Google\Cloud\Spanner\Database;
    use Google\Cloud\Spanner\SpannerClient;
    use Google\Cloud\Spanner\Result;
    use Google\Cloud\Spanner\StructType;
    use Google\Cloud\Spanner\StructValue;
    
    $spanner = new SpannerClient(['projectId' => 'my-project']);
    $database = $spanner->connect('my-instance', 'my-database');
    
    $res = $database->execute('SELECT * FROM UNNEST(ARRAY(SELECT @structParam))', [
        'parameters' => [
            'structParam' => (new StructValue)
                ->add('foo', 'bar')
                ->add('foo', 2)
                ->addUnnamed('this field is unnamed')
        ],
        'types' => [
            'structParam' => (new StructType)
                ->add('foo', Database::TYPE_STRING)
                ->add('foo', Database::TYPE_INT64)
                ->addUnnamed(Database::TYPE_STRING)
        ]
    ])->rows(Result::RETURN_NAME_VALUE_PAIR)->current();
    
    echo $res[0]['name'] . ': ' . $res[0]['value'] . PHP_EOL; // "foo: bar"
    echo $res[1]['name'] . ': ' . $res[1]['value'] . PHP_EOL; // "foo: 2"
    echo $res[2]['name'] . ': ' . $res[2]['value'] . PHP_EOL; // "2: this field is unnamed"
    

## Namespace

Google \ Cloud \ Spanner

## Methods 

### __construct

**Parameter**  
---  
**Name** | **Description**  
`values` |  `array[]`   
An array containing a field value. Each value must be of form `[(string|null) $name, mixed $value]`.  
  
### add

Add a single value to the struct.

Example:
    
    
    $structValue->add('firstName', 'John');
    

**Parameters**  
---  
**Name** | **Description**  
`name` |  `string|null`   
The struct field name.  
`value` |  `mixed`   
The struct field value.  
**Returns**  
---  
**Type** | **Description**  
`[StructValue](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/StructValue)` | The current instance, for chaining additional struct values.  
  
### addUnnamed

Add an unnamed value to the struct.

Example:
    
    
    $structValue->addUnnamed('John');
    

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
The struct field value.  
**Returns**  
---  
**Type** | **Description**  
`[StructValue](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/StructValue)` | The current instance, for chaining additional struct values.  
  
### values

Get the list of values.

**Returns**  
---  
**Type** | **Description**  
`array[]` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
