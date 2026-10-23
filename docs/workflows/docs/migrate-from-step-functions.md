---
url: https://docs.cloud.google.com/workflows/docs/migrate-from-step-functions/
title: Migrate from AWS Step Functions to Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:12.643639+00:00
---

# Migrate from AWS Step Functions to Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/migrate-from-step-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Migrate from AWS Step Functions to Workflows Stay organized with collections  Save and categorize content based on your preferences. 

To help you prepare to migrate from Amazon Web Services (AWS) Step Functions to Workflows on Google Cloud, this page explains key similarities and differences between the two products. This information is intended to assist those who are already familiar with Step Functions implement a similar architecture using Workflows.

Like Step Functions, Workflows is a fully managed, state-based orchestration platform that executes services in an order that you define: a _workflow_. These workflows can combine services including custom services hosted on Cloud Run or Cloud Run functions, Google Cloud services such as Cloud Vision AI and BigQuery, and any HTTP-based API.

Note that Step Functions _Express Workflows_ is an AWS Step Functions workflow type that is not considered here since the duration of an Express Workflow is limited, and an exactly-once workflow execution is not supported.

### Hello world

In Step Functions, a state machine is a workflow, and a task is a state in a workflow that represents a single unit of work that another AWS service performs. Step Functions requires every state to define the next state.

In Workflows, a series of steps using the Workflows syntax describes the tasks to execute. Workflows treats steps as if they are in an ordered list and executes them one at a time until all the steps have run.

The following "Hello world" sample demonstrates the use of _states_ in Step Functions and _steps_ in Workflows:

### Step Functions
    
    
      {
        "Comment": "Hello world example of Pass states in Amazon States Language",
        "StartAt": "Hello",
        "States": {
          "Hello": {
            "Type": "Pass",
            "Result": "Hello",
            "Next": "World"
          },
          "World": {
            "Type": "Pass",
            "Result": "World",
            "End": true
          }
        }
      }

### Workflows YAML
    
    
      ---
      # Hello world example of steps using Google Cloud Workflows syntax
      main:
          steps:
          - Hello:
              next: World
          - World:
              next: end
      ...

### Workflows JSON
    
    
      {
        "main": {
          "steps": [
            {
              "Hello": {
                "next": "World"
              }
            },
            {
              "World": {
                "next": "end"
              }
            }
          ]
        }
      }

**Tip:** As YAML doesn't require an end marker, it can be problematic detecting whether or not the YAML has been inadvertently truncated. The examples on this page use three dashes (`---`) to indicate the start of a workflow and three dots (`...`) to mark its end. 

## Comparison overview

This section compares the two products in more detail.

| Step Functions| Workflows  
---|---|---  
Syntax| JSON (YAML in tooling) | YAML or JSON  
Control flow| Transition among states | Imperative flow control with steps  
Worker| Resources (ARN) and HTTP task | HTTP requests and connectors  
Reliability| Catch/retry | Catch/retry  
Parallelism| Supported | Supported  
State data| State is passed along | Workflows variables  
Authentication| IAM | IAM  
User experience| Workflow Studio, CLI, SDK, IaC | Google Cloud console, CLI, SDK, IaC  
Pricing | [ Step Functions pricing](https://aws.amazon.com/step-functions/pricing/) | [Workflows pricing](https://docs.cloud.google.com/workflows/pricing)  
  
Syntax
    

Step Functions primarily uses JSON to define functions and does not support YAML directly; however, in the AWS Toolkit for Visual Studio Code and in AWS CloudFormation, you can use YAML for a Step Functions definition.

    

You can describe Workflows steps using the Workflows syntax, and they can be written in either YAML or JSON. The majority of workflows are in YAML. The examples on this page demonstrate the advantages of YAML, including ease of reading and writing, and native support of comments. For a detailed explanation of the Workflows syntax, see the [Syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax).

Control flow
    

Both Workflows and Step Functions model workflows as a series of tasks: _steps_ in Workflows and _states_ in Step Functions. Both allow a task to indicate which task to execute next and support switch-like conditionals to pick the next unit of work based on the current state. One key difference is that Step Functions requires every state to define the next one, while Workflows executes steps in the order that they are specified (including alternative next steps). For more information, see [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions) and [Steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps).

Worker
    

Both products orchestrate compute resources such as functions, containers, and other web services to get things done. In Step Functions, the worker is identified by a `Resource` field which is syntactically a URI. The URIs used to identify worker resources are in Amazon Resource Name (ARN) format. To directly invoke an arbitrary HTTP endpoint, you can define an [HTTP task](https://docs.aws.amazon.com/step-functions/latest/dg/call-https-apis.html).

    

Workflows can [send HTTP requests](https://docs.cloud.google.com/workflows/docs/http-requests) to an arbitrary HTTP endpoint and get a response. [Connectors](https://docs.cloud.google.com/workflows/docs/connectors) make it easier to connect to other Google Cloud APIs within a workflow, and to integrate your workflows with other Google Cloud products like Pub/Sub, BigQuery, or Cloud Build. Connectors simplify calling services because they handle the formatting of requests for you, providing methods and arguments so that you don't need to know the details of a Google Cloud API. You can also configure the timeout and polling policies.

Reliability
    

If a task fails, your workflow must be able to retry appropriately, catch exceptions when it has to, and reroute the workflow as necessary. Both Step Functions and Workflows achieve reliability using similar mechanisms: exception catching with retries, and eventual dispatching to elsewhere in the workflow. For more information, see [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types).

Parallelism
    

You might want your workflow to orchestrate multiple tasks in parallel. Step Functions provides two ways to achieve this: you can take one data item and pass it in parallel to multiple different tasks; or, you can use an array and pass its elements to the same task.

    

In Workflows, you can define a part of your workflow where two or more steps can execute concurrently. You can define either branches that run concurrently, or a loop where iterations run concurrently. For details, see [Execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps).

State data
    

One benefit of a workflow engine is that state data is maintained for you without an external datastore. In Step Functions, the state data is passed along in a JSON structure from one state to another.

    

In Workflows, you can save the state data in global variables. Since you are allowed up to a one-year [execution duration](https://docs.cloud.google.com/workflows/quotas), you can keep the state data as long as the instance is still in execution.

Authentication
    

Both products rely upon an underlying Identity and Access Management (IAM) system for authentication and access control. For example, you can use an IAM role to invoke Step Functions.

    

In Workflows, you can use a service account to invoke a workflow; you can use OAuth 2.0 or OIDC to connect with Google Cloud APIs; and you can use an authorization request header to authenticate with a third-party API. For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication) and [Make authenticated requests from a workflow](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow).

User experience
    

You can use a command-line tool, or infrastructure as code (IaC) such as Terraform, to define and manage both Step Functions and Workflows.

    

In addition, Workflows supports the execution of workflows using the client libraries, in the Google Cloud console, using the Google Cloud CLI, or by sending a request to the Workflows REST API. For details, see [Execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow).

Pricing
    

Both products have a free tier. For more details, see their respective pricing pages: [Step Functions pricing](https://aws.amazon.com/step-functions/pricing/) and [Workflows pricing](https://cloud.google.com/workflows/pricing).

## Mapping state types to steps

There are eight state types in Step Functions. States are elements in a state machine that can make decisions based on their input, perform actions, and pass output to other states. Before migrating from Step Functions to Workflows, ensure that you understand how to translate each state type to a Workflows step.

### `Choice`

A `Choice` state adds branching logic to a state machine.

In Workflows, you can use a `switch` block as a selection mechanism that allows the value of an expression to control the flow of a workflow's execution. If a value matches, that condition's statement is executed. For more information, see [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions).

### Step Functions
    
    
      "ChoiceState": {
        "Type": "Choice",
        "Choices": [
          {
            "Variable": "$.foo",
            "NumericEquals": 1,
            "Next": "FirstMatchState"
          },
          {
            "Variable": "$.foo",
            "NumericEquals": 2,
            "Next": "SecondMatchState"
          }
        ],
        "Default": "DefaultState"
      }

### Workflows YAML
    
    
      switch:
        - condition: ${result.body.SomeField < 10}
          next: small
        - condition: ${result.body.SomeField < 100}
          next: medium
        - condition: true
          next: default_step

### Workflows JSON
    
    
      {
        "switch": [
          {
            "condition": "${result.body.SomeField < 10}",
            "next": "small"
          },
          {
            "condition": "${result.body.SomeField < 100}",
            "next": "medium"
          },
          {
            "condition": true,
            "next": "default_step"
          }
        ]
      }

### `Fail`

A `Fail` state stops the execution of the state machine and marks it as a failure.

In Workflows, you can raise custom errors using the `raise` syntax, and you can catch and handle errors using a `try/except` block. For more information, see [Raise errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors).

### Step Functions
    
    
      "FailState": {
          "Type": "Fail",
          "Error": "ErrorA",
          "Cause": "Kaiju attack"
      }

### Workflows YAML
    
    
      raise:
          code: 55
          message: "Something went wrong."

### Workflows JSON
    
    
      {
        "raise": {
          "code": 55,
          "message": "Something went wrong."
        }
      }

### `Map`

A `Map` state can be used to run a set of steps for each element of an input array.

In Workflows, you can use a `for` loops for [iterations](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration).

### Step Functions
    
    
      { "StartAt": "ExampleMapState",
        "States": {
          "ExampleMapState": {
            "Type": "Map",
            "Iterator": {
               "StartAt": "CallLambda",
               "States": {
                 "CallLambda": {
                   "Type": "Task",
                   "Resource": "arn:aws:lambda:us-east-1:123456789012:function:HelloFunction",
                   "End": true
                 }
               }
            }, "End": true
          }
        }
      }

### Workflows YAML
    
    
      - assignStep:
          assign:
            - map:
                1: 10
                2: 20
                3: 30
            - sum: 0
      - loopStep:
          for:
              value: key
              in: ${keys(map)}
              steps:
                - sumStep:
                    assign:
                      - sum: ${sum + map[key]}
      - returnStep:
          return: ${sum}

### Workflows JSON
    
    
      [
        {
          "assignStep": {
            "assign": [
              {
                "map": {
                  "1": 10,
                  "2": 20,
                  "3": 30
                }
              },
              {
                "sum": 0
              }
            ]
          }
        },
        {
          "loopStep": {
            "for": {
              "value": "key",
              "in": "${keys(map)}",
              "steps": [
                {
                  "sumStep": {
                    "assign": [
                      {
                        "sum": "${sum + map[key]}"
                      }
                    ]
                  }
                }
              ]
            }
          }
        },
        {
          "returnStep": {
            "return": "${sum}"
          }
        }
      ]

### `Parallel`

A `Parallel` state can be used to create parallel branches of execution in your state machine. In the following Step Functions example, an address and phone lookup is performed in parallel.

In Workflows, you can use a `parallel` step to define a part of your workflow where two or more steps can execute concurrently. For more information, see [Parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps).

### Step Functions
    
    
      { "StartAt": "LookupCustomerInfo",
        "States": {
          "LookupCustomerInfo": {
            "Type": "Parallel",
            "End": true,
            "Branches": [
              {
               "StartAt": "LookupAddress",
               "States": {
                 "LookupAddress": {
                   "Type": "Task",
                   "Resource": "arn:aws:lambda:us-east-1:123456789012:function:AddressFinder",
                   "End": true
                 }
               }
             },
             {
               "StartAt": "LookupPhone",
               "States": {
                 "LookupPhone": {
                   "Type": "Task",
                   "Resource": "arn:aws:lambda:us-east-1:123456789012:function:PhoneFinder",
                   "End": true
                 }
               }
             }
            ]
          }
        }
      }

### Workflows YAML
    
    
      main:
         params: [args]
         steps:
         - init:
             assign:
             - workflow_id: "lookupAddress"
             - customer_to_lookup:
                 - address: ${args.customerId}
                 - phone: ${args.customerId}
             - addressed: ["", ""] # to write to this variable, you must share it
         - parallel_address:
             parallel:
                 shared: [addressed]
                 for:
                     in: ${customer_to_lookup}
                     index: i # optional, use if index is required
                     value: arg
                     steps:
                     - address:
                         call: googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run
                         args:
                             workflow_id: ${workflow_id}
                             argument: ${arg}
                         result: r
                     - set_result:
                         assign:
                         - addressed[i]: ${r}
         - return:
                 return: ${addressed}

### Workflows JSON
    
    
      {
        "main": {
          "params": [
            "args"
          ],
          "steps": [
            {
              "init": {
                "assign": [
                  {
                    "workflow_id": "lookupAddress"
                  },
                  {
                    "customer_to_lookup": [
                      {
                        "address": "${args.customerId}"
                      },
                      {
                        "phone": "${args.customerId}"
                      }
                    ]
                  },
                  {
                    "addressed": [
                      "",
                      ""
                    ]
                  }
                ]
              }
            },
            {
              "parallel_address": {
                "parallel": {
                  "shared": [
                    "addressed"
                  ],
                  "for": {
                    "in": "${customer_to_lookup}",
                    "index": "i",
                    "value": "arg",
                    "steps": [
                      {
                        "address": {
                          "call": "googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run",
                          "args": {
                            "workflow_id": "${workflow_id}",
                            "argument": "${arg}"
                          },
                          "result": "r"
                        }
                      },
                      {
                        "set_result": {
                          "assign": [
                            {
                              "addressed[i]": "${r}"
                            }
                          ]
                        }
                      }
                    ]
                  }
                }
              }
            },
            {
              "return": {
                "return": "${addressed}"
              }
            }
          ]
        }
      }

### `Pass`

A `Pass` state passes its input to its output, without performing work. This is commonly used to manipulate the state data in the JSON.

As Workflows does not pass along data in this way, you can leave the state as a no-op, or you can use an assign step to modify the variables. For more information, see [Assign variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step).

### Step Functions
    
    
      "No-op": {
        "Type": "Pass",
        "Result": {
          "x-datum": 0.38,
          "y-datum": 622.22
        },
        "ResultPath": "$.coords",
        "Next": "End"
      }

### Workflows YAML
    
    
      assign:
          - number: 5
          - number_plus_one: ${number+1}
          - other_number: 10
          - string: "hello"

### Workflows JSON
    
    
      {
        "assign": [
          {
            "number": 5
          },
          {
            "number_plus_one": "${number+1}"
          },
          {
            "other_number": 10
          },
          {
            "string": "hello"
          }
        ]
      }

### Succeed

A `Succeed` state stops an execution successfully.

In Workflows, you can use `return` in the main workflow to stop a workflow's execution. You can also finish a workflow by completing the final step (assuming that the step doesn't jump to another), or you can use `next: end` to stop a workflow's execution if you don't need to return a value. For more information, see [Complete the execution of a workflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing).

### Step Functions
    
    
      "SuccessState": {
        "Type": "Succeed"
      }

### Workflows YAML
    
    
      return: "Success!"
      next: end

### Workflows JSON
    
    
      {
        "return": "Success!",
        "next": "end"
      }

### `Task`

A `Task` state represents a single unit of work performed by a state machine. In the following Step Functions example, it invokes a Lambda function. (_Activities_ are an AWS Step Functions feature that enables you to have a task in your state machine where the work is performed elsewhere.)

In the Workflows example, a [call is made to an HTTP endpoint](https://docs.cloud.google.com/workflows/docs/http-requests) to invoke a Cloud Run function. You can also use a [connector](https://docs.cloud.google.com/workflows/docs/connectors) which allows easy access to other Google Cloud products. Additionally, you can [pause a workflow and poll for data](https://docs.cloud.google.com/workflows/docs/sleeping). Or, you can use a [callback endpoint](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) to signal to your workflow that a specified event has occurred, and wait on that event without polling.

### Step Functions
    
    
      "HelloWorld": {
        "Type": "Task",
        "Resource": "arn:aws:lambda:us-east-1:123456789012:function:HelloFunction",
        "End": true
      }

### Workflows YAML
    
    
      - HelloWorld:
          call: http.get
          args:
              url: https://REGION-PROJECT_ID.cloudfunctions.net/helloworld
          result: helloworld_result

### Workflows JSON
    
    
      [
        {
          "HelloWorld": {
            "call": "http.get",
            "args": {
              "url": "https://REGION-PROJECT_ID.cloudfunctions.net/helloworld"
            },
            "result": "helloworld_result"
          }
        }
      ]

### `Wait`

A `Wait` state delays the state machine from continuing for a specified time.

You can use the Workflows `sys.sleep` [standard library function](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep) to suspend execution for the given number of seconds to a maximum of 31536000 (one year).

### Step Functions
    
    
      "wait_ten_seconds" : {
        "Type" : "Wait",
        "Seconds" : 10,
        "Next": "NextState"
      }

### Workflows YAML
    
    
      - someSleep:
          call: sys.sleep
          args:
              seconds: 10

### Workflows JSON
    
    
      [
        {
          "someSleep": {
            "call": "sys.sleep",
            "args": {
              "seconds": 10
            }
          }
        }
      ]

## Example: Orchestrate microservices

The following Step Functions example checks a stock price, determines whether to buy or sell, and reports the result. The state machine in the sample integrates with AWS Lambda by passing parameters, uses an Amazon SQS queue to request human approval, and uses an Amazon SNS topic to return the results of the query.
    
    
    {
          "StartAt": "Check Stock Price",
          "Comment": "An example of integrating Lambda functions in Step Functions state machine",
          "States": {
              "Check Stock Price": {
                  "Type": "Task",
                  "Resource": "CHECK_STOCK_PRICE_LAMBDA_ARN",
                  "Next": "Generate Buy/Sell recommendation"
              },
              "Generate Buy/Sell recommendation": {
                  "Type": "Task",
                  "Resource": "GENERATE_BUY_SELL_RECOMMENDATION_LAMBDA_ARN",
                  "ResultPath": "$.recommended_type",
                  "Next": "Request Human Approval"
              },
              "Request Human Approval": {
                  "Type": "Task",
                  "Resource": "arn:PARTITION:states:::sqs:sendMessage.waitForTaskToken",
                  "Parameters": {
                      "QueueUrl": "REQUEST_HUMAN_APPROVAL_SQS_URL",
                      "MessageBody": {
                          "Input.$": "$",
                          "TaskToken.$": "$$.Task.Token"
                      }
                  },
                  "ResultPath": null,
                  "Next": "Buy or Sell?"
              },
              "Buy or Sell?": {
                  "Type": "Choice",
                  "Choices": [
                      {
                          "Variable": "$.recommended_type",
                          "StringEquals": "buy",
                          "Next": "Buy Stock"
                      },
                      {
                          "Variable": "$.recommended_type",
                          "StringEquals": "sell",
                          "Next": "Sell Stock"
                      }
                  ]
              },
              "Buy Stock": {
                  "Type": "Task",
                  "Resource": "BUY_STOCK_LAMBDA_ARN",
                  "Next": "Report Result"
              },
              "Sell Stock": {
                  "Type": "Task",
                  "Resource": "SELL_STOCK_LAMBDA_ARN",
                  "Next": "Report Result"
              },
              "Report Result": {
                  "Type": "Task",
                  "Resource": "arn:PARTITION:states:::sns:publish",
                  "Parameters": {
                      "TopicArn": "REPORT_RESULT_SNS_TOPIC_ARN",
                      "Message": {
                          "Input.$": "$"
                      }
                  },
                  "End": true
              }
          }
      }
    

### Migrate to Workflows

To migrate the preceding Step Functions example to Workflows, you can create the equivalent Workflows steps by integrating [Cloud Run functions](https://docs.cloud.google.com/workflows/docs/calling-run-functions), supporting a [callback endpoint](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) that waits for HTTP requests to arrive at that endpoint, and using a Workflows [connector to publish to a Pub/Sub topic](https://docs.cloud.google.com/workflows/docs/reference/googleapis/pubsub/Overview) in place of the Amazon SNS topic:

  1. Complete the steps to [create a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow) but do not deploy it yet.

  2. In the workflow's definition, add a step to create a callback endpoint that waits for human input, and a step that uses a Workflows connector to publish to a Pub/Sub topic. For example:

### Workflows YAML
         
         ---
           main:
             steps:
               - init:
                   assign:
                     - projectId: '${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}'
                     - region: LOCATION
                     - topic: PUBSUB_TOPIC_NAME
               - Check Stock Price:
                   call: http.get
                   args:
                     url: ${"https://" + region + "-" + projectId + ".cloudfunctions.net/CheckStockPrice"}
                     auth:
                       type: OIDC
                   result: stockPriceResponse
               - Generate Buy/Sell Recommendation:
                   call: http.get
                   args:
                     url: ${"https://" + region + "-" + projectId + ".cloudfunctions.net/BuySellRecommend"}
                     auth:
                       type: OIDC
                     query:
                       price: ${stockPriceResponse.body.stock_price}
                   result: recommendResponse
               - Create Approval Callback:
                   call: events.create_callback_endpoint
                   args:
                       http_callback_method: "GET"
                   result: callback_details
               - Print Approval Callback Details:
                   call: sys.log
                   args:
                       severity: "INFO"
                       text: ${"Listening for callbacks on " + callback_details.url}
               - Await Approval Callback:
                   call: events.await_callback
                   args:
                       callback: ${callback_details}
                       timeout: 3600
                   result: approvalResponse
               - Approval?:
                   try:
                     switch:
                       - condition: ${approvalResponse.http_request.query.response[0] == "yes"}
                         next: Buy or Sell?
                   except:
                     as: e
                     steps:
                       - unknown_response:
                           raise: ${"Unknown response:" + e.message}
                           next: end
               - Buy or Sell?:
                   switch:
                     - condition: ${recommendResponse.body == "buy"}
                       next: Buy Stock
                     - condition: ${recommendResponse.body == "sell"}
                       next: Sell Stock
                     - condition: true
                       raise: ${"Unknown recommendation:" + recommendResponse.body}
               - Buy Stock:
                   call: http.post
                   args:
                     url: ${"https://" + region + "-" + projectId + ".cloudfunctions.net/BuyStock"}
                     auth:
                       type: OIDC
                     body:
                       action: ${recommendResponse.body}
                   result: message
               - Sell Stock:
                   call: http.post
                   args:
                     url: ${"https://" + region + "-" + projectId + ".cloudfunctions.net/SellStock"}
                     auth:
                       type: OIDC
                     body:
                       action: ${recommendResponse.body}
                   result: message
               - Report Result:
                   call: googleapis.pubsub.v1.projects.topics.publish
                   args:
                     topic: ${"projects/" + projectId + "/topics/" + topic}
                     body:
                       messages:
                       - data: '${base64.encode(json.encode(message))}'
                   next: end
           ...

### Workflows JSON
         
         {
             "main": {
               "steps": [
                 {
                   "init": {
                     "assign": [
                       {
                         "projectId": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
                       },
                       {
                         "region": "LOCATION"
                       },
                       {
                         "topic": [
                           "PUBSUB_TOPIC_NAME"
                         ]
                       }
                     ]
                   }
                 },
                 {
                   "Check Stock Price": {
                     "call": "http.get",
                     "args": {
                       "url": "${\"https://\" + region + \"-\" + projectId + \".cloudfunctions.net/CheckStockPrice\"}",
                       "auth": {
                         "type": "OIDC"
                       }
                     },
                     "result": "stockPriceResponse"
                   }
                 },
                 {
                   "Generate Buy/Sell Recommendation": {
                     "call": "http.get",
                     "args": {
                       "url": "${\"https://\" + region + \"-\" + projectId + \".cloudfunctions.net/BuySellRecommend\"}",
                       "auth": {
                         "type": "OIDC"
                       },
                       "query": {
                         "price": "${stockPriceResponse.body.stock_price}"
                       }
                     },
                     "result": "recommendResponse"
                   }
                 },
                 {
                   "Create Approval Callback": {
                     "call": "events.create_callback_endpoint",
                     "args": {
                       "http_callback_method": "GET"
                     },
                     "result": "callback_details"
                   }
                 },
                 {
                   "Print Approval Callback Details": {
                     "call": "sys.log",
                     "args": {
                       "severity": "INFO",
                       "text": "${\"Listening for callbacks on \" + callback_details.url}"
                     }
                   }
                 },
                 {
                   "Await Approval Callback": {
                     "call": "events.await_callback",
                     "args": {
                       "callback": "${callback_details}",
                       "timeout": 3600
                     },
                     "result": "approvalResponse"
                   }
                 },
                 {
                   "Approval?": {
                     "try": {
                       "switch": [
                         {
                           "condition": "${approvalResponse.http_request.query.response[0] == \"yes\"}",
                           "next": "Buy or Sell?"
                         }
                       ]
                     },
                     "except": {
                       "as": "e",
                       "steps": [
                         {
                           "unknown_response": {
                             "raise": "${\"Unknown response:\" + e.message}",
                             "next": "end"
                           }
                         }
                       ]
                     }
                   }
                 },
                 {
                   "Buy or Sell?": {
                     "switch": [
                       {
                         "condition": "${recommendResponse.body == \"buy\"}",
                         "next": "Buy Stock"
                       },
                       {
                         "condition": "${recommendResponse.body == \"sell\"}",
                         "next": "Sell Stock"
                       },
                       {
                         "condition": true,
                         "raise": "${\"Unknown recommendation:\" + recommendResponse.body}"
                       }
                     ]
                   }
                 },
                 {
                   "Buy Stock": {
                     "call": "http.post",
                     "args": {
                       "url": "${\"https://\" + region + \"-\" + projectId + \".cloudfunctions.net/BuyStock\"}",
                       "auth": {
                         "type": "OIDC"
                       },
                       "body": {
                         "action": "${recommendResponse.body}"
                       }
                     },
                     "result": "message"
                   }
                 },
                 {
                   "Sell Stock": {
                     "call": "http.post",
                     "args": {
                       "url": "${\"https://\" + region + \"-\" + projectId + \".cloudfunctions.net/SellStock\"}",
                       "auth": {
                         "type": "OIDC"
                       },
                       "body": {
                         "action": "${recommendResponse.body}"
                       }
                     },
                     "result": "message"
                   }
                 },
                 {
                   "Report Result": {
                     "call": "googleapis.pubsub.v1.projects.topics.publish",
                     "args": {
                       "topic": "${\"projects/\" + projectId + \"/topics/\" + topic}",
                       "body": {
                         "messages": [
                           {
                             "data": "${base64.encode(json.encode(message))}"
                           }
                         ]
                       }
                     },
                     "next": "end"
                   }
                 }
               ]
             }
           }

Replace the following:

     * `LOCATION`: a supported [Google Cloud region](https://docs.cloud.google.com/workflows/docs/locations). For example, `us-central1`.
     * `PUBSUB_TOPIC_NAME`: the name of your Pub/Sub topic. For example, `my_stock_example`.
  3. Deploy and then [execute the workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow).

  4. During the workflow's execution, it pauses and waits for you to invoke the callback endpoint. You can use a curl command to do this. For example:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
         https://workflowexecutions.googleapis.com/v1/projects/CALLBACK_URL?response=yes
         

Replace `CALLBACK_URL` with the rest of the path to your callback endpoint.

  5. Once the workflow has successfully completed, you can [receive the message from the Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/create-topic-gcloud#receive_messages). For example:
         
         gcloud pubsub subscriptions pull stock_example-sub  --format="value(message.data)" | jq
         

The output message should be similar to the following (either a `buy` or a `sell`):
         
         {
           "body": "buy",
           "code": 200,
           "headers": {
           [...]
           }
         




## What's next

  * [Workflows overview](https://docs.cloud.google.com/workflows/docs/overview)
  * [Create and manage workflows](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow)
  * [Sample workflows](https://docs.cloud.google.com/workflows/docs/samples)
  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
