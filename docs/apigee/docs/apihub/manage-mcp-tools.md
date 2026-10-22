---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-tools/
title: Manage MCP tools \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:19.569343+00:00
---

# Manage MCP tools  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage MCP tools Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to add and manage MCP tools for MCP APIs. MCP APIs are designed for AI agents, and are registered with the **MCP** API style. You can import MCP APIs from Apigee or register them manually. For more information, see [Register MCP APIs](https://docs.cloud.google.com/apigee/docs/apihub/register-mcp-apis). 

## Add MCP tools using the API

### REST

To add a MCP tool to an API version, use the [Create operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations/create) API.
    
    
    curl --location 'https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/apis/API_ID/versions/VERSION_ID/operations?api_operation_id=TOOL_ID' \
    --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    --header 'Content-Type: application/json; charset=utf-8' \
    --data '{
        "details": {
          "description": "DESCRIPTION",
          "documentation": {
            "externalUri": "EXTERNAL_URI"
          },
          "deprecated": false,
          "mcpTool": {
            "name": "TOOL_NAME",
            "title": "TOOL_TITLE",
            "description": "TOOL_DESCRIPTION",
            "annotations": {
              "title": "TOOL_ANNOTATION_TITLE",
              "readOnlyHint": false,
              "destructiveHint": false,
              "idempotentHint": true,
              "openWorldHint": false,
              "additionalHints": {
                "custom_hint": "TOOL_ANNOTATION_CUSTOM_HINT"
              }
            },
            "inputSchema": {
            "jsonSchema": {  
              "type": "object",
              "properties": {
                "input_param": {
                  "type": "string"
                }
              }
            }
          },
          "outputSchema": {
            "jsonSchema": { 
              "type": "object",
              "properties": {
                "output_result": {
                  "type": "string"
                }
              }
            }
          }
          }
        }
      }'
    

Replace the following:

  * `PROJECT`: your Google Cloud project ID.
  * `LOCATION`: the location of your API.
  * `API_ID`: the ID of your API.
  * `VERSION_ID`: the ID of the API version.
  * `TOOL_ID`: the ID of the tool.
  * `DESCRIPTION`: a description of the tool.
  * `EXTERNAL_URI`: a URI that provides more information about the tool.
  * `TOOL_NAME`: the name of the tool. This field is required and must not be empty. It's used to generate the operation ID.
  * `TOOL_TITLE`: a human-readable title for the tool.
  * `TOOL_DESCRIPTION`: a description of what the tool does.
  * `TOOL_ANNOTATION_TITLE`: an annotation title for the tool.
  * `TOOL_ANNOTATION_CUSTOM_HINT`: a custom hint for the tool.



### Example
    
    
    curl --location 'https://apihub.googleapis.com/v1/projects/apihub-test-api/locations/us-central1/apis/apihub-test-api/versions/1/operations?api_operation_id=get-weather' \
    --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    --header 'Content-Type: application/json; charset=utf-8' \
    --data '{
        "details": {
          "description": "Fetches the current weather for a given location.",
          "documentation": {
            "externalUri": "https://www.example.com/weather"
          },
          "deprecated": false,
          "mcpTool": {
            "name": "get-weather",
            "title": "Get Weather",
            "description": "Fetches the current weather for a given location.",
            "annotations": {
              "title": "Weather Tool",
              "readOnlyHint": true,
              "destructiveHint": false,
              "idempotentHint": true,
              "openWorldHint": true,
              "additionalHints": {
                "apiProvider": "Some Weather API"
              }
            },
            "inputSchema": {
              "jsonSchema": {
                "type": "object",
                "properties": {
                  "location": {
                    "type": "string",
                    "description": "The city and state, e.g., San Francisco, CA"
                  }
                },
                "required": [
                  "location"
                ]
              }
            },
            "outputSchema": {
              "jsonSchema": {
                "type": "object",
                "properties": {
                  "temperature": {
                    "type": "number"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      }'
    

## Extract MCP tools from Apigee MCP proxies

**Private Preview — MCP in Apigee**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

API hub automatically imports all MCP proxies created in your associated Apigee organization. These proxies are registered with the **MCP** API style, and their specification files are parsed to extract MCP tools. 

To see the MCP tools extracted from a specific proxy, go to the **API hub > APIs** page, select an API, and then select a version. The **MCP Tools** section lists all the tools extracted from the proxies associated with that API. 

**Important:**

  * When Apigee MCP proxies are imported, API hub identifies the associated OpenAPI Specification (OAS) files as MCP specs and parses them to extract MCP tools. While the specification type is updated to **MCP** , the underlying OAS file is not currently converted to the MCP specification schema. This is a known issue.
  * For Apigee MCP proxies with multiple deployment revisions, API hub only parses MCP tools from the latest deployed revision. Tools from earlier revisions are not available or supported.



## Add MCP tools using a specification file

MCP tools are automatically extracted from the MCP specification file when you add it to a version of a registered MCP API.

### Console

To add MCP tools using a specification file, do the following:

  1. In the Google Cloud console, go to the **API hub > APIs** page. 

[ Go to APIs](https://console.cloud.google.com/apigee/api-hub/apis)

  2. Click the API for which you want to attach a specification file.
  3. Create a new API version or select an existing one. 
  4. On the **Versions** page, click **Add specification**.
  5. In the **Add specification file** pane, configure the following: 
     * **Specification file ID** : Click **Specify Unique ID** to enter a custom ID. If omitted, one is generated automatically. **Note:** Specification ID must be 4-500 characters long and can contain only uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and hyphens (-). The ID forms the last part of the API resource name: `projects/PROJECT/locations/LOCATION/apis/API_ID/versions/VERSION_ID/specs/SPEC_ID`. The full resource name is limited to 1000 characters.
     * **Display name** : Enter a name for the specification file.
     * **Specification file type** : Select **MCP Schema**.
     * **Specification document** : Click **Browse** to upload the MCP specification JSON file. **Notes:**
       * The specification file must be a valid JSON file conforming to the sample MCP specification file schema.
       * The specification file must contain a `tools` array.
       * The `name` field of each tool is required. MCP tools without a `name` field are ignored while parsing.
       * The `name` field of each tool must be unique. If duplicates are found, the MCP tool with the last instance of the duplicate `name` is used.
     * **Restrict upload of spec file containing errors** : **Don't** select this checkbox. **Caution:** Selecting this checkbox may prevent the specification file from being uploaded due to current validation limitations.
  6. Click **Create**.

The MCP specification file is parsed and the tools are listed in the **MCP Tools** section of the version details page. 




The following image shows the **MCP Tools** section of the version details page: 

![MCP tools section of the version details page](https://docs.cloud.google.com/static/apigee/docs/apihub/images/mcp-tools.png)

## MCP specification file schema

### JSON schema

The following JSON schema shows the structure of a valid MCP specification file. 
    
    
    {
      "type": "object",
      "properties": {
        "tools": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the tool. This field is REQUIRED and must not be empty. It's used to generate the operation ID."
              },
              "title": {
                "type": "string",
                "description": "A human-readable title for the tool. Optional."
              },
              "description": {
                "type": "string",
                "description": "A description of what the tool does. Optional."
              },
              "inputSchema": {
                "type": "object",
                "description": "A JSON Schema object describing the input parameters for the tool. Optional. Can be any valid JSON object.",
                "additionalProperties": true
              },
              "outputSchema": {
                "type": "object",
                "description": "A JSON Schema object describing the output structure of the tool. Optional. Can be any valid JSON object.",
                "additionalProperties": true
              },
              "annotations": {
                "type": "object",
                "description": "Optional annotations for the tool.",
                "properties": {
                  "title": {
                    "type": "string",
                    "description": "Annotation title. Optional."
                  },
                  "readOnlyHint": {
                    "type": "boolean",
                    "description": "Hint indicating if the tool is read-only. Optional."
                  },
                  "destructiveHint": {
                    "type": "boolean",
                    "description": "Hint indicating if the tool can have destructive side effects. Optional."
                  },
                  "idempotentHint": {
                    "type": "boolean",
                    "description": "Hint indicating if the tool is idempotent. Optional."
                  },
                  "openWorldHint": {
                    "type": "boolean",
                    "description": "Hint indicating if the tool interacts with the open world. Optional."
                  },
                  "additionalHints": {
                    "type": "object",
                    "description": "A map of additional string key-value hints. Optional.",
                    "additionalProperties": {
                      "type": "string"
                    }
                  }
                },
                "additionalProperties": false
              }
            },
            "required": [
              "name"
            ],
            "additionalProperties": false
          },
          "description": "A list of tool objects. This array is REQUIRED at the top level."
        },
        "resources": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          },
          "description": "Optional array of resource objects. The parser doesn't strictly define their content."
        },
        "prompts": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          },
          "description": "Optional array of prompt objects. The parser doesn't strictly define their content."
        },
        "errors": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          },
          "description": "Optional array of error objects. The parser doesn't strictly define their content."
        }
      },
      "required": [
        "tools"
      ],
      "additionalProperties": false
    }

### Example

The following example shows a valid MCP specification file using the sample JSON schema. 
    
    
    {
      "tools": [
        {
          "name": "get-weather",
          "title": "Get Weather",
          "description": "Fetches the current weather for a given location.",
          "inputSchema": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g., San Francisco, CA"
              }
            },
            "required": [
              "location"
            ]
          },
          "outputSchema": {
            "type": "object",
            "properties": {
              "temperature": {
                "type": "number"
              },
              "unit": {
                "type": "string"
              },
              "description": {
                "type": "string"
              }
            }
          },
          "annotations": {
            "title": "Weather Tool",
            "readOnlyHint": true,
            "destructiveHint": false,
            "idempotentHint": true,
            "openWorldHint": true,
            "additionalHints": {
              "apiProvider": "Some Weather API"
            }
          }
        },
        {
          "name": "send-email",
          "title": "Send Email",
          "description": "Sends an email."
        },
        {
          "name": "tool with spaces and Upper"
        }
      ],
      "resources": [],
      "prompts": [],
      "errors": []
    }

## What's next

  * See the API reference documentation for the [Operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations) API.
  * Learn more about [API specifications](https://docs.cloud.google.com/apigee/docs/apihub/specs-intro).
  * Learn more about [API operations and MCP tools](https://docs.cloud.google.com/apigee/docs/apihub/operations-intro).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
