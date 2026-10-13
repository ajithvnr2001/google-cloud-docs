---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/maps/
title: Maps \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:54.406917+00:00
---

# Maps  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/maps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Maps Stay organized with collections  Save and categorize content based on your preferences. 

Workflows supports maps (dictionaries) that can hold a user-defined structure of variables or lists.

For other map processing functions, see the Workflows standard library [`map` module reference](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview#module:-map).

## Map definition

To define a map, add an assign step to the workflow:

### YAML
    
    
      - STEP_NAME_A:
          assign:
            - MAP_A:
                KEY_1: VALUE_1
                KEY_2:
                    KEY_3: VALUE_2

### JSON
    
    
      [
        {
          "STEP_NAME_A": {
            "assign": [
              {
                "MAP_A": {
                  "KEY_1": "VALUE_1",
                  "KEY_2": {
                    "KEY_3": "VALUE_2"
                  }
                }
              }
            ]
          }
        }
      ]

For example:

### YAML
    
    
    - createMap:
        assign:
          - dynamicKey: "MiddleName"
          - myMap:
              FirstName: "John"
              ${dynamicKey}: "Apple"
              LastName: "Smith"
              Age: 26
              Address:
                Street: "Flower Road 12"
                City: "Superville"
                Country: "Atlantis"

### JSON
    
    
    [
      {
        "createMap": {
          "assign": [
            {
              "dynamicKey": "MiddleName"
            },
            {
              "myMap": {
                "FirstName": "John",
                "${dynamicKey}": "Apple",
                "LastName": "Smith",
                "Age": 26,
                "Address": {
                  "Street": "Flower Road 12",
                  "City": "Superville",
                  "Country": "Atlantis"
                }
              }
            }
          ]
        }
      }
    ]

If a key name includes non-alphanumeric characters (for example, the exclamation point in `"special!key": value`), you must wrap the key name in quotes. For more information, in this document, see Access key names with non-alphanumeric characters.

Similarly, when using dynamic keys in a map defined with braces, wrap the expression in quotes (single or double) so that it is YAML-compliant. For example:

### YAML
    
    
      - createMap:
          assign:
            - dynamicKey: "myKey"
            - myMap: {"${dynamicKey}": "myValue"}
            - myMap2: {'${dynamicKey + "Apple"}': "myValue"}

### JSON
    
    
      [
        {
          "createMap": {
            "assign": [
              {
                "dynamicKey": "myKey"
              },
              {
                "myMap": {
                  "${dynamicKey}": "myValue"
                }
              },
              {
                "myMap2": {
                  "${dynamicKey + \"Apple\"}": "myValue"
                }
              }
            ]
          }
        }
      ]

## Read map values

To read the values in a map, use one of the following structures within an expression:
    
    
    ${MAP.KEY}
    ${MAP[KEY_EXPRESSION]}

### Access nested keys

Use an additional period or index to access the value of a nested key. For example, to return the value of `Country` from the previous example:

### YAML
    
    
      - lastStep:
          return: ${myMap.Address.Country}

### JSON
    
    
      [
        {
          "lastStep": {
            "return": "${myMap.Address.Country}"
          }
        }
      ]

### Access key names with non-alphanumeric characters

When accessing key names with non-alphanumeric characters (for example, the exclamation point in `"special!key": value`), you must wrap the key name in quotes:

### YAML
    
    
      - createMap:
          assign:
          - var:
              key:
                  "special!key": bar
      - lastStep:
          return: '${"foo" + var.key["special!key"]}'

### JSON
    
    
      [
        {
          "createMap": {
            "assign": [
              {
                "var": {
                  "key": {
                    "special!key": "bar"
                  }
                }
              }
            ]
          }
        },
        {
          "lastStep": {
            "return": "${\"foo\" + var.key[\"special!key\"]}"
          }
        }
      ]

### Perform a safe lookup on a map

You can use the standard library function, [`map.get`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/get), to perform a safe lookup on a map, returning `null` if the key is not found. For example:

### YAML
    
    
      - lastStep:
          return: ${default(map.get(myMap, "FirstName"), "Couldn't find key!")}

### JSON
    
    
      [
        {
          "lastStep": {
            "return": "${default(map.get(myMap, \"FirstName\"), \"Couldn't find key!\")}"
          }
        }
      ]

For nested maps, a list of keys can be used to drill down into the map, using a nested key lookup. For example, `map.get(my2DMap, ["key1", "key2"])` is equivalent to `map.get(map.get(my2DMap, "key1"), "key2")`.

## Insert and update map values

Use an `assign` step to update existing keys, or to assign a value to a new key.

Using index notation allows the use of expressions as the key. Note that the expression must evaluate to a string during execution.

### YAML
    
    
      - update_map:
          assign:
              - my_map: {"Key1": "hello"}
              - key_str: "Key"
              - my_map.Key1: "Value1"
              - my_map["Key2"]: "Value2"
              - my_map[key_str]: "Value3"
              - my_map[key_str + "4"]: "Value4"

### JSON
    
    
      [
        {
          "update_map": {
            "assign": [
              {
                "my_map": {
                  "Key1": "hello"
                }
              },
              {
                "key_str": "Key"
              },
              {
                "my_map.Key1": "Value1"
              },
              {
                "my_map[\"Key2\"]": "Value2"
              },
              {
                "my_map[key_str]": "Value3"
              },
              {
                "my_map[key_str + \"4\"]": "Value4"
              }
            ]
          }
        }
      ]

You can create and update nested map values:

### YAML
    
    
      - update_nested_map:
          assign:
              - my_map: {}
              - my_map.NestedMapKey: {"Key1":"Value1"}
              - my_map.NestedMapKey.Key2: "Value2"

### JSON
    
    
      [
        {
          "update_nested_map": {
            "assign": [
              {
                "my_map": {}
              },
              {
                "my_map.NestedMapKey": {
                  "Key1": "Value1"
                }
              },
              {
                "my_map.NestedMapKey.Key2": "Value2"
              }
            ]
          }
        }
      ]

You can update map keys dynamically in a `for` loop:

### YAML
    
    
      - update_map_in_loop:
          assign:
            - keys: ["key1", "key2"]
            - my_map: {}
      - for_loop:
          for:
            value: v
            index: i
            in: ${keys}
            steps:
              - loop_step:
                  assign:
                    - my_map[v]: ${i}
      - return_step:
          return: ${my_map}

### JSON
    
    
      [
        {
          "update_map_in_loop": {
            "assign": [
              {
                "keys": [
                  "key1",
                  "key2"
                ]
              },
              {
                "my_map": {}
              }
            ]
          }
        },
        {
          "for_loop": {
            "for": {
              "value": "v",
              "index": "i",
              "in": "${keys}",
              "steps": [
                {
                  "loop_step": {
                    "assign": [
                      {
                        "my_map[v]": "${i}"
                      }
                    ]
                  }
                }
              ]
            }
          }
        },
        {
          "return_step": {
            "return": "${my_map}"
          }
        }
      ]

The result of the preceding workflow should be `{"key1":0,"key2":1}`.

## Check existence of a key in a map

To check whether a given key is present in a map, use the following expression: 
    
    
    ${KEY in MAP}

For example:

### YAML
    
    
      - MyStep:
          switch:
            - condition: ${"Age" in myMap}
              next: AgeExists

### JSON
    
    
      [
        {
          "MyStep": {
            "switch": [
              {
                "condition": "${\"Age\" in myMap}",
                "next": "AgeExists"
              }
            ]
          }
        }
      ]

To check whether a key is not in a map, use the `not()` function:

### YAML
    
    
      - MyStep:
          switch:
            - condition: ${not("Age" in myMap)}
              next: AgeMissing

### JSON
    
    
      [
        {
          "MyStep": {
            "switch": [
              {
                "condition": "${not(\"Age\" in myMap)}",
                "next": "AgeMissing"
              }
            ]
          }
        }
      ]

## Get the length of a map

You can get the length of a map by using the `len()` [expression helper](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#data_type_functions). This built-in function accepts an attribute of type `map` and returns the number of elements in the map as an integer. For example, the following sample returns `2`:

### YAML
    
    
      - init:
          assign:
            - my_map: {"key1": "hello", "key2": "world"}
      - returnStep:
          return: ${len(my_map)}  # returns `2`

### JSON
    
    
      [
        {
          "init": {
            "assign": [
              {
                "my_map": {
                  "key1": "hello",
                  "key2": "world"
                }
              }
            ]
          }
        },
        {
          "returnStep": {
            "return": "${len(my_map)}"
          }
        }
      ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
