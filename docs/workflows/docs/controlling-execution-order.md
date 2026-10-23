---
url: https://docs.cloud.google.com/workflows/docs/controlling-execution-order/
title: Control the order of execution in a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:13.431433+00:00
---

# Control the order of execution in a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/controlling-execution-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Control the order of execution in a workflow Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use jumps or for loops to control the order in which your workflow's steps run. Basic jumps allow you to define which step the workflow runs next. Conditional jumps build on basic jumps, allowing you to use conditional [expressions](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions) to control the order of execution through a workflow. For example, you can run certain steps only when a variable or response from another workflow step meets specific criteria.

The examples on this page use a sample API that returns the day of the week.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. You should already have an existing workflow where you want to change the order of execution. To learn how to create and deploy a workflow, see [Create and update a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow).



## Use jumps to change execution order

By default, all workflows are ordered lists where every step runs in the order you define in the workflow's source code. You can choose to override this default ordering by using jumps.

### Basic jumps

You can specify which step to run next in a workflow by using basic jumps.

### Console

  1. Open the Workflows page in the Google Cloud console:   
[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Select the name of the workflow where you want to change the order of execution of the existing steps.

  3. On the **Edit workflow** page, select **Next** to go to the workflow editor.

  4. Add the `next` field at the end of a step to tell the workflow to jump to a particular step:

### YAML
         
         - step_a:
                  ...
                  next: STEP_NAME_TO_JUMP_TO
              - step_b:
                  ...
              - next_step:
                  ...

### JSON
         
         [
               {
                 "step_a": {
                   ...
                   "next": "STEP_NAME_TO_JUMP_TO"
                 }
               }
               {
                 "step_b": {
                   ...
                 }
               }
               {
                 "next_step": {
                   ...
                 }
               }
             ]

Replace `STEP_NAME_TO_JUMP_TO` with the name of the step you want the workflow to execute next. For example, `next_step`.

  5. Select **Deploy**.




### gcloud

  1. Open your workflow's definition file in the text editor of your choice.

  2. Add the `next` field at the end of a step to tell the workflow to jump to a particular step:

### YAML
         
         - step_a:
                  ...
                  next: STEP_NAME_TO_JUMP_TO
              - step_b:
                  ...
              - next_step:
                  ...

### JSON
         
         [
             {
               "step_a": {
                 ...
                 "next": "STEP_NAME_TO_JUMP_TO"
               }
             }
             {
               "step_b": {
                 ...
               }
             }
             {
               "next_step": {
                 ...
               }
             }
           ]

Replace `STEP_NAME_TO_JUMP_TO` with the name of the step you want the workflow to execute next. For example, `next_step`.

  3. Save the workflow file.

  4. To deploy the workflow, enter the following command:
         
         gcloud workflows deploy WORKFLOW_NAME \
         --source=WORKFLOW_FILE.YAML

Replace the following:

     * `WORKFLOW_NAME`: required. The name of your workflow.

     * `WORKFLOW_FILE.YAML`: required. The source file for the workflow.




### Example

For example, the following workflow has its steps out of order:

### YAML
    
    
      - get_time:
         call: http.get
         args:
             url:  https://us-central1-workflowsample.cloudfunctions.net/datetime
         result: currentTime
      - return_daylight_savings_bool:
         return: ${daylightSavings}
      - get_daylight_savings_bool:
         assign:
             - daylightSavings: ${currentTime.body.isDayLightSavingsTime}

### JSON
    
    
        [
          {
            "get_time": {
              "call": "http.get",
              "args": {
                "url": "https://us-central1-workflowsample.cloudfunctions.net/datetime"
              },
              "result": "currentTime"
            }
          },
          {
            "return_daylight_savings_bool": {
              "return": "${daylightSavings}"
            }
          },
          {
            "get_daylight_savings_bool": {
              "assign": [
                {
                  "daylightSavings": "${currentTime.body.isDayLightSavingsTime}"
                }
              ]
            }
          }
        ]

In this example, `next` fields have been added to the `get_daylight_savings_bool` and `return_daylight_savings_bool` steps so that the steps execute in the correct order:

### YAML
    
    
      - get_time:
         call: http.get
         args:
             url:  https://us-central1-workflowsample.cloudfunctions.net/datetime
         result: currentTime
         next: get_daylight_savings_bool
      - return_daylight_savings_bool:
         return: ${daylightSavings}
      - get_daylight_savings_bool:
         assign:
             - daylightSavings: ${currentTime.body.isDayLightSavingsTime}
         next: return_daylight_savings_bool

### JSON
    
    
        [
          {
            "get_time": {
              "call": "http.get",
              "args": {
                "url": "https://us-central1-workflowsample.cloudfunctions.net/datetime"
              },
              "result": "currentTime",
              "next": "get_daylight_savings_bool"
            }
          },
          {
            "return_daylight_savings_bool": {
              "return": "${daylightSavings}"
            }
          },
          {
            "get_daylight_savings_bool": {
              "assign": [
                {
                  "daylightSavings": "${currentTime.body.isDayLightSavingsTime}"
                }
              ],
              "next": "return_daylight_savings_bool"
            }
          }
        ]

### Conditional jumps

You can use conditional jumps to determine which step to run next in a workflow. Conditional jumps use `switch` blocks, which jump to a specified step if a particular [condition](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions) is met. Each `switch` block can include a maximum of 50 conditions.

### Console

  1. Open the Workflows page in the Google Cloud console:   
[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Select the name of the workflow to which you want to add a `switch` block.

  3. On the **Edit workflow** page, select **Next** to go to the workflow editor.

  4. On the **Define workflow** page, your workflow's current definition is displayed. To edit the workflow so that it executes a certain step based on a conditional statement, add a step that uses a `switch` block:

### YAML
         
         - SWITCH_STEP_NAME:
                  switch:
                      - condition: ${EXPRESSION_ONE}
                        next: STEP_A
                      - condition: ${EXPRESSION_TWO}
                        next: STEP_B
                      ...
                  next: STEP_C
              - STEP_A
                  ...
              - STEP_B
                  ...
              - STEP_C
                  ...

### JSON
         
         [
               {
                 "SWITCH_STEP_NAME": {
                   "switch": [
                     {
                       "condition": "${EXPRESSION_ONE}",
                       "next": "STEP_A"
                     },
                     {
                       "condition": "${EXPRESSION_TWO}",
                       "next": "STEP_B"
                     }
                   ],
                   "next": "STEP_C"
                 }
                 "STEP_A": {
                   ...
                 }
                 "STEP_B": {
                   ...
                 }
                 "STEP_C": {
                   ...
                 }
               }
             ]

Replace the following:

     * `SWITCH_STEP_NAME`: the name of the step containing the `switch` block.

     * `EXPRESSION_ONE`: the first expression to evaluate. If this expression evaluates to true, the workflow executes `STEP_A` next. If this expression evaluates to false, the workflow evaluates the next expression.

     * `EXPRESSION_TWO`: the second expression to evaluate. If this expression evaluates to true, the workflow executes `STEP_B` next. If this expression evaluates to false, the workflow executes `STEP_C`.

     * `STEP_A`, `STEP_B`, `STEP_C`: placeholder step names.

  5. Select **Deploy**.




### gcloud

  1. Open your workflow's definition in the text editor of your choice.

  2. To edit the workflow so that it executes a certain step based on a conditional statement, add a step that uses a `switch` block:

### YAML
         
         - SWITCH_STEP_NAME:
              switch:
                  - condition: ${EXPRESSION_ONE}
                    next: STEP_A
                  - condition: ${EXPRESSION_TWO}
                    next: STEP_B
                  ...
              next: STEP_C
          - STEP_A
              ...
          - STEP_B
              ...
          - STEP_C
              ...

### JSON
         
         [
           {
             "SWITCH_STEP_NAME": {
               "switch": [
                 {
                   "condition": "${EXPRESSION_ONE}",
                   "next": "STEP_A"
                 },
                 {
                   "condition": "${EXPRESSION_TWO}",
                   "next": "STEP_B"
                 }
               ],
               "next": "STEP_C"
             }
             "STEP_A": {
               ...
             }
             "STEP_B": {
               ...
             }
             "STEP_C": {
               ...
             }
           }
         ]
           

Replace the following:

     * `SWITCH_STEP_NAME`: the name of the step containing the `switch` block.

     * `EXPRESSION_ONE`: the first expression to evaluate. If this expression evaluates to true, the workflow executes `STEP_A` next. If this expression evaluates to false, the workflow evaluates the next expression.

     * `EXPRESSION_TWO`: the second expression to evaluate. If this expression evaluates to true, the workflow executes `STEP_B` next. If this expression evaluates to false, the workflow executes `STEP_C`.

     * `STEP_A`, `STEP_B`, `STEP_C`: placeholder step names.

  3. Save the workflow file.

  4. To deploy the workflow, enter the following command:
         
         gcloud workflows deploy WORKFLOW_NAME \
         --source=WORKFLOW_FILE.YAML

Replace the following:

     * `WORKFLOW_NAME`: required. The name of your workflow.

     * `WORKFLOW_FILE.YAML`: required. The source file for the workflow.




### Example

For example, this workflow uses a switch block to control the workflow's order of execution:

### YAML
    
    
      - getCurrentTime:
          call: http.get
          args:
              url:  https://us-central1-workflowsample.cloudfunctions.net/datetime
          result: currentTime
      - conditionalSwitch:
          switch:
              - condition: ${currentTime.body.dayOfTheWeek == "Friday"}
                next: friday
              - condition: ${currentTime.body.dayOfTheWeek == "Saturday" OR currentTime.body.dayOfTheWeek == "Sunday"}
                next: weekend
          next: workWeek
      - friday:
          return: "It's Friday! Almost the weekend!"
      - weekend:
          return: "It's the weekend!"
      - workWeek:
          return: "It's the work week."
        

### JSON
    
    
        [
          {
            "getCurrentTime": {
              "call": "http.get",
              "args": {
                "url": "https://us-central1-workflowsample.cloudfunctions.net/datetime"
              },
              "result": "currentTime"
            }
          },
          {
            "conditionalSwitch": {
              "switch": [
                {
                  "condition": "${currentTime.body.dayOfTheWeek == "Friday"}",
                  "next": "friday"
                },
                {
                  "condition": "${currentTime.body.dayOfTheWeek == "Saturday" OR currentTime.body.dayOfTheWeek == "Sunday"}",
                  "next": "weekend"
                }
              ],
              "next": "workWeek"
            }
          },
          {
            "friday": {
              "return": "It's Friday! Almost the weekend!"
            }
          },
          {
            "weekend": {
              "return": "It's the weekend!"
            }
          },
          {
            "workWeek": {
              "return": "It's the work week."
            }
          }
        ]
          

In this example, the `switch` block has two conditions. The parser evaluates each condition in order, and if the result of the condition's expression is `true`, that condition's `next` step is called. If none of the conditions are met, the workflow calls the step specified by the `next` field outside of the `switch` block, which, in this example, is the step `workWeek`.

For example, if the day of the week is `"Saturday"`, then the workflow jumps to the step `weekend` and returns the message `"It's the weekend!"`. The workflow doesn't execute the step `friday` because the conditional jump skips over it, and the workflow doesn't execute the step `workWeek` because `return` stops the execution of the workflow at the end of the `weekend` step.

## Use `for` loops to iterate

You can use `for` loops to iterate over a sequence of numbers or through a collection of data, such as a list or map.

You can walk through every item in a list or map using item-based iteration. If you have a specific range of numeric values to iterate through, you can use range-based iteration.

For more information and examples, see the syntax reference on [iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration).

## What's next

  * [Execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
