---
url: https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments/
title: Pass runtime arguments in an execution request \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:10.091952+00:00
---

# Pass runtime arguments in an execution request  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Pass runtime arguments in an execution request Stay organized with collections  Save and categorize content based on your preferences. 

Workflows lets you supply dynamic input to an execution using runtime arguments, which your workflow accesses through variables. This helps you adapt execution logic and process varying event payloads without modifying the workflow definition.

**Note:** The [maximum size of the arguments](https://docs.cloud.google.com/workflows/quotas) you can pass to a workflow execution is 512 KB.

## Set up a workflow that receives runtime arguments

To set up a workflow to receive runtime arguments that you pass to it as part of an execution request, do the following:

  1. Follow the steps to [create](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#creating_a_workflow) a new workflow, or choose an existing workflow to [update](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#updating_a_workflow), but don't deploy it yet.

  2. Add a `params` field to the main workflow's definition. Ensure that the argument name is placed inside square brackets, and that the main workflow is placed in a `main` block:

### YAML
         
         main:
           params: [ARG_NAME]
           steps:
             ...

### JSON
         
         {
           "main": {
             "params": ["ARG_NAME"],
             "steps": [
               ...
             ]
             ...
           }
         }
           

The `main` block accepts a single argument that is the name of any valid JSON data type; for example, an array, an object, or a string.

As a best practice, passing in an object with multiple, named arguments makes it easier to understand their purpose, and to add arguments. You can also then use dot notation to access the arguments.

Other subworkflows can have multiple arguments.

For example, the following workflow returns a "Hello" greeting to a person whose first and last name you pass as runtime arguments:

### YAML
         
         main:
           params: [args]
           steps:
             - step1:
                 assign:
                   - outputVar: ${"Hello, " + args.firstName + " " + args.lastName + "!"}
             - step2:
                 return: ${outputVar}

### JSON
         
         {
           "main": {
             "params": [
               "args"
             ],
             "steps": [
               {
                 "step1": {
                   "assign": [
                     {
                       "outputVar": "${\"Hello \" + args.firstName + \" \" + args.lastName}"
                     }
                   ]
                 }
               },
               {
                 "step2": {
                   "return": "${outputVar}"
                 }
               }
             ]
           }
         }
           

  3. Deploy your workflow to finish creating or updating it.




## Pass data in an execution request

Once your workflow is set up to receive runtime arguments, you can pass a string in JSON format, such as `{"firstName":"Workflows","lastName":"User"}`, to the workflow in an execution request.

### Console

  1. To execute a workflow, in the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, select a workflow to go to its details page.

  3. On the **Workflow Details** page, click _play_arrow_ **Execute**.

  4. On the "Execute workflow" page that displays, enter a JSON string containing your parameter names and argument values, such as `{"firstName":"Workflows","lastName":"User"}`, into the "Input" area:

![Input area populated with the example JSON string](https://docs.cloud.google.com/static/workflows/images/argument-execution-console.png)

  5. Click **Execute**.

On the **Execution details** page, you can view the results of the execution including the output **`Hello, Workflows User!`** , the execution ID and state, and the current or final step of the workflow execution. For more information, see [Access workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results).




### gcloud

Add the [\--data](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/execute#--data) flag to the [gcloud workflows execute](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/execute) command that you use to execute your workflow. This flag takes a JSON string of your data. For example, to pass a `firstName` and `lastName` to the previous example workflow:
    
    
    gcloud workflows run WORKFLOW_NAME \
    --data='{"firstName":"FIRST","lastName":"LAST"}'

Replace the following:

  * `WORKFLOW_NAME`: the workflow's name
  * `FIRST`: the string you want to pass to your workflow for `firstName`
  * `LAST`: the string you want to pass to your workflow for `lastName`



The output should be similar to the following:
    
    
    Waiting for execution [9379b067-306a-4db1-a58d-c9fc99aebfd4] to complete...done.
    argument: '{"firstName":"Workflows","lastName":"User"}'
    endTime: '2022-07-19T13:52:47.659199466Z'
    name: projects/1051295516635/locations/us-central1/workflows/workflow-6/executions/9379b067-306a-4db1-a58d-c9fc99aebfd4
    result: '"Hello, Workflows User!"'
    startTime: '2022-07-19T13:52:47.623862835Z'
    state: SUCCEEDED
    status:
      currentSteps:
      - routine: main
        step: step2
    workflowRevisionId: 000002-138
    

### Client libraries

Depending on the client library language, you can pass a runtime argument in an execution request.

For example, using JavaScript:
    
    
    // Execute workflow
    try {
      const createExecutionRes = await client.createExecution({
        parent: client.workflowPath(projectId, location, workflow),
        execution: {
          argument: JSON.stringify({"firstName":"Workflows","lastName":"User"})
        }
    });
    const executionName = createExecutionRes[0].name;
    

Or, using Java:
    
    
    // Creates the execution object.
    CreateExecutionRequest request =
        CreateExecutionRequest.newBuilder()
            .setParent(parent.toString())
            .setExecution(Execution.newBuilder().setArgument("{\"firstName\":\"Workflows\",\"lastName\":\"User\"}").build())
            .build();
    

For more information about executing a workflow using the Google API Client Libraries, see [Execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow#execute_a_workflow).

### REST API

  1. Append the `data` flag to the command that you use to execute your workflow. The value of `data` is a JSON formatted string with an argument whose value is one or more escaped parameter-value pairs. For example, to pass a `firstName` and `lastName` to the previous example workflow:
         
         curl --request POST \
            --header "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
            --header 'Content-Type: application/json' \
            --data '{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}' \
            "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/us-central1/workflows/WORKFLOW_NAME/executions"

Replace the following:

     * `PROJECT_NUMBER`: your Google Cloud project number
     * `WORKFLOW_NAME`: the workflow's name
     * `FIRST`: the string you want to pass to your workflow for `firstName`
     * `LAST`: the string you want to pass to your workflow for `lastName`

The output should be similar to the following:
    
    {
      "name": "projects/PROJECT_NUMBER/locations/us-central1/workflows/WORKFLOW_NAME/executions/EXECUTION_ID",
      "startTime": "2020-11-09T23:51:31.765761331Z",
      "state": "ACTIVE",
      "argument": "{\"firstName\":\"Workflows\",\"lastName\":\"User\"}",
      "workflowRevisionId": "000001-08c"
    }
     ```
    

  2. To get the execution results, run the following command:
         
         curl --request GET \
            --header "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
            --header 'Content-Type: application/json' \
            "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/us-central1/workflows/WORKFLOW_NAME/executions/EXECUTION_ID"
         

Replace `EXECUTION_ID` with the ID from the output your first command returned.

This output contains lines similar to the following:
         
         "argument": "{\"firstName\":\"Workflows\",\"lastName\":\"User\"}",
         "result": "\"Hello, Workflows User!\"",
         




For more information about executing a workflow using the REST API, see [Execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow#rest-api).

## Access runtime arguments

This sample accesses runtime arguments passed to the workflow as part of the execution request. All arguments are stored in the same map, declared as a parameter of the main workflow.

When running this workflow, pass in runtime arguments using the following format:
    
    
    {"firstName":"Sherlock", "lastName":"Holmes"}
    

### YAML
    
    
    main:
      params: [args]
      steps:
        - step1:
            assign:
              - outputVar: ${"Hello " + args.firstName + " " + args.lastName}
        - step2:
            return: ${outputVar}

### JSON
    
    
    {
      "main": {
        "params": [
          "args"
        ],
        "steps": [
          {
            "step1": {
              "assign": [
                {
                  "outputVar": "${\"Hello \" + args.firstName + \" \" + args.lastName}"
                }
              ]
            }
          },
          {
            "step2": {
              "return": "${outputVar}"
            }
          }
        ]
      }
    }

You can use `default` with the standard library function, [map.get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/get), to access optional runtime arguments, and return a default value if the key is not found. In the following example, if a `region` is not specified, `northamerica-northeast1` is used:

### YAML
    
    
      main:
          params: [input]
          steps:
          - init:
              assign:
                - region: ${default(map.get(input, "region"), "northamerica-northeast1")}
      

### JSON
    
    
      {
        "main": {
          "params": [
            "input"
          ],
          "steps": [
            {
              "init": {
                "assign": [
                  {
                    "region": "${default(map.get(input, \"region\"), \"northamerica-northeast1\")}"
                  }
                ]
              }
            }
          ]
        }
      }

## What's next

  * [Create and manage workflows](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow)
  * [Schedule a workflow using Cloud Scheduler](https://docs.cloud.google.com/workflows/docs/schedule-workflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
