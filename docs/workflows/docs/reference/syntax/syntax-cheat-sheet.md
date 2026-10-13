---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/syntax-cheat-sheet/
title: Syntax cheat sheet \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:44.058319+00:00
---

# Syntax cheat sheet  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/syntax-cheat-sheet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Syntax cheat sheet Stay organized with collections  Save and categorize content based on your preferences. 

The following workflow provides a concise overview of the [Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax) that can be used for quick reference. For more information, click the links in the workflow. You can also download the printable PDF:

[ ![Workflows syntax cheat sheet](https://docs.cloud.google.com/static/workflows/images/cheat-sheet-thumbnail.png)](https://docs.cloud.google.com/static/workflows/images/workflows-cheat-sheet-pr96.pdf)
    
    
    [main](https://docs.cloud.google.com/workflows/docs/reference/syntax#main):
      [params](https://docs.cloud.google.com/workflows/docs/reference/syntax#params): [[args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args)]
      [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
        # [Runtime arguments](https://docs.cloud.google.com/workflows/docs/reference/syntax/runtime-args)
        - read_runtime_args:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - arg1: ${args.arg1}
              - arg2: ${args.arg2}
        # [Variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables) and [data types](https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes)
        - data_types:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - my_integer: 1      # 64 bit, signed
              - my_double: 4.1     # 64 bit, signed floating point number
              - my_string: "hello" # unicode <= 256 KB length
              - my_boolean: true   # true/false, True/False, TRUE/FALSE
              - my_null: null
              - my_list: ["zero","one","two"]
              - my_map:
                  name: Alex
                  last_name: Taylor
                  birthYear: 1990
        - conversion_functions:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - to_double: double("2.7") # string, integer to double
              - to_int: int(2.7)         # string, double to integer
              - to_string: string(1.7)   # int, double, boolean to string
        # [Boolean](https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes)
        - logical_ops:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - my_true: true
              - my_false: false
              - my_false: ${my_true and my_false}
              - my_true: ${my_true or my_false}
              - my_false: ${not my_true}
        # [Strings](https://docs.cloud.google.com/workflows/docs/reference/syntax/strings)
        - string_ops:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - my_string: "hello"
              - string_len: ${len(my_string)}
              - string_plus_string: ${my_string+" "+"world"}
              - string_plus_int: ${my_string+" "+string(my_integer)}
              - string_escaped: '${"a: " +my_string}'
        # [Lists](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists)
        - list_ops:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - my_list: ["zero","one","two"]
              - my_list_len: ${len(my_list)}
              - key_exists: ${"Key1" in my_list}
              - my_list[0]: 0
              - idx: 0
              - my_list[idx + 1]: 1
              - my_list[my_list_len - 1]: 2
              - my_list: ${list.concat(my_list, 3)}
              - my_multi_dimen_list: [[10, 11, 12], [20, 21, 22]]
              - my_multi_dimen_list[0][1]: "Value11"
        # [Maps](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps)
        - map_ops:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - my_map: {"Key1": "hello"}
              - map_len: ${len(my_map)}
              - key_exists: ${"Key1" in my_map}
              - key_list: ${keys(my_map)}
              - key_is_null: ${default(map.get(my_map, "Key1"), "Couldn't find key!")}
              - key_with_special_char: '${"fruit" + var.key["special!key"]}'
              - key_str: "Key"
              - my_map.Key1: "Value1"
              - my_map["Key2"]: "Value2"
              - my_map[key_str + "3"]: "Value3"
              - my_nested_map: {"NestedMapKey": {"Key1":"Value1"}}
              - my_nested_map.NestedMapKey.Key2: "Value2"
        # [Jumps](https://docs.cloud.google.com/workflows/docs/reference/syntax/jumps)
        - step_with_next:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - fruit: "apple"
            [next](https://docs.cloud.google.com/workflows/docs/reference/syntax#next): step_with_nested_steps
        # [Complete execution](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing)
        - step_with_end:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
               - fruit: "apple"
            [next](https://docs.cloud.google.com/workflows/docs/reference/syntax#next): [end](https://docs.cloud.google.com/workflows/docs/reference/syntax#end)
        # [Nested steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps#embedded-steps)
        - step_with_nested_steps:
            [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                - nested_step_1:
                    [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                      - fruit: "apple"
                - nested_step_2:
                    [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                      - fruit: "apple"
        # [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)
        - for-in-list:
            [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
              - assignList:
                  [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                      - list: [1, 2, 3, 4, 5]
                      - sum: 0
              - loopList:
                  [for](https://docs.cloud.google.com/workflows/docs/reference/syntax#for):
                      value: v
                      in: ${list}
                      [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                          - sumList:
                              [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                                  - sum: ${sum + v}
        - for-in-map:
            [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
              - assignMap:
                  [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                      - map: {1: 10, 2: 20, 3: 30}
                      - sum: 0
              - loopMap:
                  [for](https://docs.cloud.google.com/workflows/docs/reference/syntax#for):
                      value: key
                      in: ${keys(map)}
                      [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                          - sumMap:
                              [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                                  - sum: ${sum + map[key]}
        - for-range:
            [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
              - assignRange:
                  [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                      - sum: 0
              - loopRange:
                  [for](https://docs.cloud.google.com/workflows/docs/reference/syntax#for):
                      value: v
                      range: [1, 9]
                      [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                          - sumRange:
                              [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                                  - sum: ${sum + v}
        # [Parallel branches](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#parallel-branch)
        - init:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - user: {}
              - notification: {}
        - parallel_branches:
            [parallel](https://docs.cloud.google.com/workflows/docs/reference/syntax#parallel):
              shared: [user, notification]
              [branches](https://docs.cloud.google.com/workflows/docs/reference/syntax#branches):
                - getUser:
                    [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                      - getUserCall:
                          [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): http.get
                          [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                            url: ${"https://example.com/users/" + args.userId}
                          [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): user
                - getNotification:
                    [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                      - getNotificationCall:
                          [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): http.get
                          [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                            url: ${"https://example.com/notification/" + args.notificationId}
                          [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): notification
        # [Parallel iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#parallel-iteration)
        - init:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - total: 0
        - parallel_loop:
            [parallel](https://docs.cloud.google.com/workflows/docs/reference/syntax#parallel):
              shared: [total]
              [for](https://docs.cloud.google.com/workflows/docs/reference/syntax#for):
                value: postId
                in: ${args.posts}
                [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                  - getPostCommentCount:
                      [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): http.get
                      [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                        url: ${"https://example.com/postComments/" + postId}
                      [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): numComments
                  - add:
                      [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                        - total: ${total + numComments}
        # [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
        - switch_basic:
            [switch](https://docs.cloud.google.com/workflows/docs/reference/syntax#switch):
              - [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax#condition): ${my_integer < 10}
                [next](https://docs.cloud.google.com/workflows/docs/reference/syntax#next): switch_embedded_steps
              - [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax#condition): ${my_boolean}
                [next](https://docs.cloud.google.com/workflows/docs/reference/syntax#next): switch_embedded_steps
              - [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax#condition): true # optional, default condition
                [next](https://docs.cloud.google.com/workflows/docs/reference/syntax#next): switch_embedded_steps
            [next](https://docs.cloud.google.com/workflows/docs/reference/syntax#next): switch_embedded_steps
        - switch_embedded_steps:
            [switch](https://docs.cloud.google.com/workflows/docs/reference/syntax#switch):
              - [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax#condition): ${my_integer < 10}
                [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                  - stepA:
                      [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                        - fruit: "apple"
                  - stepB:
                      [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
                        - fruit: "apple"
        # [Subworkflows](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows)
        - call_subworkflow:
            [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): subworkflow_name_message
            [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                first_name: "Alex"
                last_name: "Taylor"
            [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): output
        - call_subworkflow2:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - output2: ${subworkflow_name_message("Sherlock","Holmes")}
        # [Raise errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
        - raise_custom_string_error:
            [raise](https://docs.cloud.google.com/workflows/docs/reference/syntax#raise): "Something went wrong."
        - raise_custom_map_error:
            [raise](https://docs.cloud.google.com/workflows/docs/reference/syntax#raise):
                code: 55
                message: "Something went wrong."
        # [Catch errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
        - try_retry_except:
            [try](https://docs.cloud.google.com/workflows/docs/reference/syntax#try):
              [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps): # steps is only needed if multiple steps
                  - step_a:
                      [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): http.get
                      [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                          url: https://host.com/api
                      [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): api_response1
                  - step_b:
                      [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): http.get
                      [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                          url: https://host.com/api2
                      [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): api_response2
            # [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying) (optional)
            # Either, you can use a retry with default policy
            # [retry](https://docs.cloud.google.com/workflows/docs/reference/syntax#retry): ${http.default_retry}
            # Or, you can use a more fine-grained policy
            # [retry](https://docs.cloud.google.com/workflows/docs/reference/syntax#retry):
            #   predicate: ${http.default_retry_predicate}
            #   max_retries: 10
            #   backoff:
            #       initial_delay: 1
            #       max_delay: 90
            #       multiplier: 3
            [except](https://docs.cloud.google.com/workflows/docs/reference/syntax#except):
                as: e
                [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
                    - known_errors:
                        [switch](https://docs.cloud.google.com/workflows/docs/reference/syntax#switch):
                        - [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax#condition): ${not("HttpError" in e.tags)}
                          [return](https://docs.cloud.google.com/workflows/docs/reference/syntax#return): "Connection problem."
                        - [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax#condition): ${e.code == 404}
                          [return](https://docs.cloud.google.com/workflows/docs/reference/syntax#return): "Sorry, URL wasn't found."
                        - [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax#condition): ${e.code == 403}
                          [return](https://docs.cloud.google.com/workflows/docs/reference/syntax#return): "Authentication error."
                    - unhandled_exception:
                        [raise](https://docs.cloud.google.com/workflows/docs/reference/syntax#raise): ${e}
        # [Standard library](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview)
        ## [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests)
        - http_get:
            [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): http.get
            [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                url: https://en.wikipedia.org/w/api.php
                headers:
                    Content-Type: "text/plain"
                query:
                    action: opensearch
                    search: monday
            [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): wikiResult
        - http_post:
            [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): http.post
            [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                url: https://us-central1-myproject123.cloudfunctions.net/myfunc1
                auth:
                    type: OIDC
                body:
                    some_val: "Hello World"
                    another_val: 123
            [result](https://docs.cloud.google.com/workflows/docs/reference/syntax#result): the_message
        ## [Function sys.log](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/log)
        - log:
            [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): sys.log
            [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
              data: ${wikiResult}
        ## [Function sys.get_env](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/get_env)
        - get_env_vars:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - projectNumber: ${sys.get_env("GOOGLE_CLOUD_PROJECT_NUMBER")}
              - projectID: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
              - workflowId: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_ID")}
              - workflowRevisionId: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_REVISION_ID")}
              - workflowExecutionId: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
        ## [Function sys.now](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/now)
        - get_now:
            [assign](https://docs.cloud.google.com/workflows/docs/reference/syntax#assign):
              - now: ${sys.now()}
        ## [Function sys.sleep](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep)
        - wait:
            [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): sys.sleep
            [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                seconds: 10
        # [Connectors](https://docs.cloud.google.com/workflows/docs/reference/googleapis)
        ## [Compute Engine API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/Overview)
        - insert_machine:
            [call](https://docs.cloud.google.com/workflows/docs/reference/syntax#call): googleapis.compute.v1.instances.insert
            [args](https://docs.cloud.google.com/workflows/docs/reference/syntax#args):
                project: ${projectID}
                zone: europe-west1-b
                body:
                  name: my-machine
                  machineType: zones/europe-west1-b/e2-small
                  disks:
                  - initializeParams:
                      sourceImage: "projects/debian-cloud/global/images/debian-10-buster-v20201112"
                    boot: true
                    autoDelete: true
                  networkInterfaces:
                  - network: "global/networks/default"
        # [Return from workflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing)
        - return_multiple_values:
            [return](https://docs.cloud.google.com/workflows/docs/reference/syntax#return):
              my_integer: ${my_integer}
              my_string: ${my_string}
              my_true: ${my_true}
              my_false: ${my_false}
              my_list: ${my_list}
              my_multi_dimen_list: ${my_multi_dimen_list}
              my_map: ${my_map}
              my_nested_map: ${my_nested_map}
        - return_single_value:
            [return](https://docs.cloud.google.com/workflows/docs/reference/syntax#return): ${my_integer}
    
    # [Subworkflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows)
    subworkflow_name_message:
        [params](https://docs.cloud.google.com/workflows/docs/reference/syntax#params): [first_name, last_name, country: "England"]
        [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax#steps):
            - prepareMessage:
                [return](https://docs.cloud.google.com/workflows/docs/reference/syntax#return): ${"Hello " + first_name + " " + last_name + " from " + country + "."}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
