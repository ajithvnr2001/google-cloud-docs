---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-multi-step-workflows-overview/
title: Multi-step workflows \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:00.101546+00:00
---

# Multi-step workflows  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-multi-step-workflows-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Multi-step workflows Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature has limited access. Contact your Google Cloud representative to access private GA features.

Companion agent provides real time guidance during live conversations to help human agents navigate complex tasks that involve multiple steps. The multistep workflows feature tracks mandatory steps and provides contextual task details to enhance agent productivity, accelerate on the job training, and maintain consistent service quality and compliance. This feature automatically detects the right step based on the progress of a conversation.

## Key features

The multistep workflows feature in a companion agent provides the following benefits:

  * **Standardized processes** : Helps every human agent to follow the exact same steps, reducing compliance errors and shortening training time.
  * **Extract details** : Captures key details automatically from customer messages, such as order numbers, dates or preferences.
  * **Automated tool initiation** : Runs system tools automatically during the conversation or waits for human agent approval before completing important tasks.
  * **Human-in-the-loop** : Human agents control each step. They can start or dismiss workflows, edit saved information, mark tasks as complete, and return to previous steps.



## How it works

Companion agent initiates multistep workflows when a human agent starts a conversation and the topic matches a particular workflow. Multistep workflows display the top 3 workflow cards with a title and instructions. For example, if a customer inquires about a technician appointment, the top 3 workflow cards would be:

  * Appointment inquiry
  * Appointment cancellation
  * Appointment scheduling



The instructions for an appointment inquiry would include steps such as:

  * Validate the customer
  * Retrieve appointment information
  * Confirm appointment details



Multistep workflows operate on proactive mode. Companion agent reads each customer message and suggests up to three relevant workflows. After the human agent launches a workflow, guidance mode tracks step completion and generates suggested replies and next actions for the active step.

## Workflow steps

Workflows consist of the following five core steps:

  1. **Tell customer** : Displays instructions and recommended responses for a human agent to share with customers.
  2. **Collect information** : Defines specific details that a human agent must collect from the customer.
  3. **Manual action** : Directs the human agent to perform an action in an external tool or desktop application and record output variables.
  4. **Tool call** : Companion agent initiates an automated system tool and saves response details in workflow variables.
  5. **End workflow** : Marks the completion of a workflow branch.



### Example workflow

The following example of _damaged item return and replacement_ demonstrates how to create a complete branching workflow, publish it as the active live version, and attach it to a companion agent.

#### Step 1: Create the workflow

The following JSON object defines the complete structure for a workflow draft:
    
    
    POST /v2beta1/projects/my-project/locations/global/companionAgentWorkflows
    
    {
      "displayName": "Damaged Item Return and Replacement",
      "description": "Use this workflow when a customer reports receiving a damaged, broken, or defective item and requests a replacement or refund.",
      "rootStepId": "step_1_collect_details",
      "steps": [
        {
          "id": "step_1_collect_details",
          "title": "Collect Order ID and Resolution Preference",
          "type": "INFORMATION_COLLECTION",
          "actions": [
            {
              "humanAgentAction": {
                "informationCollectionAction": {
                  "displayDetails": {
                    "content": "Ask the customer for their **Order ID** and whether they prefer a **Replacement** or a **Refund**.",
                    "enableMarkdown": true
                  },
                  "messageSuggestionConfig": {
                    "content": "Ask the customer for their order number and whether they would like a free replacement or a full refund.",
                    "verbatim": false
                  },
                  "variables": [
                    {
                      "name": "order_id",
                      "description": "The customer's alphanumeric order identifier (for example, ORD-5510).",
                      "stringType": {}
                    },
                    {
                      "name": "resolution_preference",
                      "description": "Whether the customer wants a replacement unit or a refund.",
                      "enumType": {
                        "values": ["REPLACEMENT", "REFUND"]
                      }
                    }
                  ]
                }
              }
            }
          ],
          "transitions": [
            {
              "targetStepId": "step_2_check_eligibility"
            }
          ]
        },
        {
          "id": "step_2_check_eligibility",
          "title": "Verify Order Return Eligibility",
          "type": "SYSTEM_ACTION",
          "actions": [
            {
              "systemAction": {
                "cesToolSpec": {
                  "cesTool": "projects/my-project/locations/global/apps/order-app/tools/lookup-order",
                  "confirmationRequirement": "NOT_REQUIRED"
                },
                "outputVariableMappings": [
                  {
                    "variable": {
                      "name": "order_eligible",
                      "description": "Whether the order is within the 30-day return window.",
                      "booleanType": {}
                    },
                      "fieldPaths": [
                      {"path": "order.returnEligible"},
                      {"path": "data.isEligible"}
                    ]
                  }
                ]
              }
            }
          ],
          "transitions": [
            {
              "targetStepId": "step_3a_log_replacement",
              "condition": {
                "variableCondition": "order_eligible == true && resolution_preference == 'REPLACEMENT'"
              }
            },
            {
              "targetStepId": "step_3b_refund_disclosure",
              "condition": {
                "variableCondition": "order_eligible == true && resolution_preference == 'REFUND'"
              }
            },
            {
              "targetStepId": "step_3c_explain_ineligible"
            }
          ]
        },
        {
          "id": "step_3a_log_replacement",
          "title": "Create Replacement Shipment in Warehouse Portal",
          "type": "MANUAL_ACTION",
          "actions": [
            {
              "humanAgentAction": {
                "manualExternalSystemAction": {
                  "displayDetails": {
                    "content": "Open the **Warehouse Portal**, select **Expedited Replacement**, and enter the new tracking number below.",
                    "enableMarkdown": true
                  },
                  "variables": [
                    {
                      "name": "replacement_tracking_id",
                      "description": "The tracking number generated in the Warehouse Portal.",
                      "stringType": {}
                    }
                  ]
                }
              }
            }
          ],
          "transitions": [
            {
              "targetStepId": "step_4_end"
            }
          ]
        },
        {
          "id": "step_3b_refund_disclosure",
          "title": "Read Mandatory Refund Disclosure",
          "type": "INFORMATIONAL_MESSAGE",
          "actions": [
            {
              "humanAgentAction": {
                "informationalResponseAction": {
                  "displayDetails": {
                    "content": "Read the required refund policy disclosure verbatim to the customer.",
                    "enableMarkdown": false
                  },
                  "messageSuggestionConfig": {
                    "content": "Your full refund has been approved. Please note that refunds take 3 to 5 business days to post to your original payment method, and the damaged item must be dropped off using the prepaid return label within 14 calendar days.",
                    "verbatim": true
                  }
                }
              }
            }
          ],
          "transitions": [
            {
              "targetStepId": "step_4_end"
            }
          ]
        },
        {
          "id": "step_3c_explain_ineligible",
          "title": "Explain Return Window Expiration",
          "type": "INFORMATIONAL_MESSAGE",
          "actions": [
            {
              "humanAgentAction": {
                "informationalResponseAction": {
                  "messageSuggestionConfig": {
                    "content": "Politely inform the customer that the 30-day return window has expired and offer a 15% courtesy discount toward a replacement.",
                    "verbatim": false
                  }
                }
              }
            }
          ],
          "transitions": [
            {
              "targetStepId": "step_4_end"
            }
          ]
        },
        {
          "id": "step_4_end",
          "title": "Complete Workflow",
          "type": "END_WORKFLOW"
        }
      ]
    }
    

#### Step 2: Publish and promote to live

Send a request to publish the draft workflow and set its status to live as in the following example:
    
    
    POST /v2beta1/projects/my-project/locations/global/companionAgentWorkflows/damaged-item-return:publish
    
    {
      "markLive": true
    }
    

#### Step 3: Attach the workflow to a companion agent

The following JSON object specifies the companion agent configuration and trigger settings for attaching the workflow:
    
    
    PATCH /v2beta1/projects/my-project/locations/global/companionAgents/my-companion-agent?updateMask=companionAgentWorkflowSpecs,skillConfigs
    
    {
      "companionAgentWorkflowSpecs": [
        {
          "workflow": "projects/my-project/locations/global/companionAgentWorkflows/damaged-item-return",
          "proactiveEnabled": true
        }
      ],
      "skillConfigs": [
        {
          "skillTriggeringEvent": "END_OF_UTTERANCE",
          "guidanceSkillConfig": {}
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
