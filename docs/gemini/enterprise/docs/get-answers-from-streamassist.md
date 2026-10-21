---
url: https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist/
title: Get search results from StreamAssist \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:11.218793+00:00
---

# Get search results from StreamAssist  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Developer guide ](https://docs.cloud.google.com/gemini/enterprise/docs/developer-guide)



Send feedback 

#  Get search results from StreamAssist Stay organized with collections  Save and categorize content based on your preferences. 

In your web app, you can get answers to your questions in the form of streaming responses. This document shows you how to use the REST API to get answers. If you want to use the Gemini Enterprise web app, see [Chat with the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat).

## `StreamAssist` overview

`StreamAssist` provides a powerful, interactive way to handle user queries. It operates in a streaming fashion, enabling real-time, back-and-forth interactions.

The key capabilities of the API include the following:

  * **Maintaining conversational context:** it uses sessions to maintain conversational context, ensuring it understands follow-up queries within the scope of previous interactions.

  * **Incorporating provided files:** it includes the attached files as context for more informed and relevant responses.

  * **Seamless integration:** it integrates with various agents and tools to fulfill a wide range of user requests.




## Before you begin

Ensure that you have the following:

  * The **Discovery Engine API** enabled for your Google Cloud. You can enable it on the **Discovery Engine API** page in the Google Cloud console.

[Go to Discovery Engine API](https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics)

  * A [Discovery Engine role](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine) that has the `discoveryengine.assistants.assist` permission assigned to it.

  * An existing Gemini Enterprise app. To create an app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).




## Get search results

You can use the [`streamAssist`](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist) method to query and get answers from Gemini Enterprise. The following curl command lists the mandatory fields.

### REST
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
      -d '
    {
      "query": {
        "text": "QUERY_TEXT_1"
      }
    }'
    

Replace the following:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * APP_ID: the unique identifier for the Gemini Enterprise app.
  * LOCATION: the multi-region of your data store: `global`, `us`, or `eu`
  * QUERY_TEXT_1: the search query text.



#### Example command and result
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant:streamAssist" \
      -d '
    {
      "query": {
        "text": "By when do corporations need to file taxes?"
      }
    }'
    
    
    * * *
    
    
    {
      "answer": {
        "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013/assistAnswers/123456789019",
        "state": "SUCCEEDED",
        "replies": [
          {
            "groundedContent": {},
            "replyId": "123456789050"
          },
          {
            "groundedContent": {},
            "replyId": "123456789050"
          }
        ],
        "diagnosticInfo": {
          "plannerSteps": [
            {
              "createTime": "2025-11-24T22:21:13.958569117Z",
              "queryStep": {
                "parts": [
                  {
                    "text": "By when do corporations need to file taxes?"
                  }
                ]
              }
            },
            {
              "createTime": "2025-11-24T22:21:17.218914056Z",
              "planStep": {
                "parts": [
                  {
                    "text": "**Formulating the Query**\n"
                  }
                ],
                "planStepId": "123456789050",
                "role": "MODEL"
              }
            },
            {
              "planStep": {
                "parts": [
                  {
                    "text": "**Refining the Response**\n"
                  }
                ],
                "role": "MODEL",
                "planStepId": "123456789050"
              },
              "createTime": "2025-11-24T22:21:19.734447578Z"
            },
            {
              "createTime": "2025-11-24T22:21:21.940682307Z",
              "planStep": {
                "planStepId": "123456789050",
                "role": "MODEL",
                "parts": [
                  {
                    "text": "**Processing the Results**\n"
                  }
                ]
              }
            },
            {
              "planStep": {
                "role": "MODEL",
                "parts": [
                  {
                    "text": "**Querying and Analyzing**\n**Structuring the Answer**\n"
                  }
                ],
                "planStepId": "123456789050"
              },
              "createTime": "2025-11-24T22:21:25.058155923Z"
            },
            {
              "createTime": "2025-11-24T22:21:25.955761161Z",
              "planStep": {
                "planStepId": "123456789050",
                "role": "MODEL",
                "parts": [
                  {
                    "text": "**Refining the Details**\n"
                  }
                ]
              }
            },
            {
              "createTime": "2025-11-24T22:21:25.967576803Z",
              "planStep": {
                "role": "MODEL",
                "parts": [
                  {
                    "text": "Of course, I can help with that. The deadline for corporations to file their federal income tax returns depends on the type of corporation.\n\n### **Corporate Tax Filing Deadlines**\n\n| Corporation Type | Deadline | For Calendar Year-End (Dec. 31) |\n| :--- | :--- | :--- |"
                  }
                ],
                "planStepId": "123456789050"
              }
            },
            {
              "createTime": "2025-11-24T22:21:25.988820408Z",
              "planStep": {
                "planStepId": "123456789050",
                "role": "MODEL",
                "parts": [
                  {
                    "text": "\n| **C Corporations** | 15th day of the fourth month after the end of their fiscal year. | April 15 |\n| **S Corporations** | 15th day of the third month after the end of their fiscal year. | March 15 |\n\n---\n\n###"
                  }
                ]
              }
            },
            {
              "createTime": "2025-11-24T22:21:26.016095651Z",
              "planStep": {
                "planStepId": "123456789050",
                "role": "MODEL",
                "parts": [
                  {
                    "text": " **Extensions**\n\nIf a corporation needs more time to file, it can request a six-month extension by filing the appropriate form with the IRS. It's important to note that an extension to file is not an extension to pay. Taxes are still due by the original deadline.\n\nWould you like to know about"
                  }
                ]
              }
            },
            {
              "planStep": {
                "parts": [
                  {
                    "text": " the deadlines for any other types of business entities?"
                  }
                ],
                "planStepId": "123456789050",
                "role": "MODEL"
              },
              "createTime": "2025-11-24T22:21:26.070810455Z"
            }
          ]
        }
      },
      "sessionInfo": {
        "session": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
        "queryId": "123456789078",
        "turnId": "123456789013_123456789029"
      },
      "assistToken": "1234567890123456789012345678901234567890"
    }
    

For more information on the fields and what is returned, see [Response body](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist#response-body).

**Note:** To continue the conversation in the same session, save the `session` value from the response and include it in your next query.

### Python

Before trying this sample, follow the Python setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Update these variables before running the sample.
    project_id = "YOUR_PROJECT_ID"
    location = "YOUR_LOCATION"
    engine_id = "YOUR_APP_ID"
    query = "What is Gemini Enterprise?"
    
    
    def stream_assist_sample(
        project_id: str,
        location: str,
        engine_id: str,
        query: str,
    ):
        # For more information, refer to:
        # https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        client = discoveryengine.AssistantServiceClient(client_options=client_options)
    
        request = discoveryengine.StreamAssistRequest(
            name=client.assistant_path(
                project=project_id,
                location=location,
                collection="default_collection",
                engine=engine_id,
                assistant="default_assistant",
            ),
            query=discoveryengine.Query(text=query),
        )
    
        # Make the request
        stream = client.stream_assist(request=request)
    
        # Handle the response
        for response in stream:
            print(response)
    

## Get search results using the same session

To continue a conversation and get answers from Gemini Enterprise within an existing session, use the [`streamAssist`](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist) method. The following code sample shows the mandatory fields:

### REST
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
      -d '
    {
      "session": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions/SESSION_ID",
      "query": {
        "text": "QUERY_TEXT_2"
      }
    }'
    

Replace the following:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * APP_ID: the unique identifier for the Gemini Enterprise app.
  * LOCATION: the multi-region of your data store: `global`, `us`, or `eu`
  * QUERY_TEXT_2: the search query text.
  * SESSION_ID: the ID of a session from a previous conversation or query.



#### Example command and result
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant:streamAssist" \
      -d '
    {
      "session": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
      "query": {
        "text": "what are the documents you need to file taxes?"
      }
    }'
    
    
    * * *
    
    
    {
      "answer": {
        "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013/assistAnswers/15195007515750046778",
        "state": "SUCCEEDED",
        "replies": [
          {
            "groundedContent": {},
            "replyId": "123456789051"
          },
          {
            "groundedContent": {},
            "replyId": "123456789051"
          }
        ],
        "diagnosticInfo": {
          "plannerSteps": [
            {
              "queryStep": {
                "parts": [
                  {
                    "text": "what are the documents you need to file taxes?"
                  }
                ]
              },
              "createTime": "2025-11-24T23:06:45.101296577Z"
            },
            {
              "planStep": {
                "role": "MODEL",
                "parts": [
                  {
                    "text": "**Identifying Tax Documents**\n"
                  }
                ],
                "planStepId": "123456789051"
              },
              "createTime": "2025-11-24T23:06:48.201642404Z"
            },
            {
              "planStep": {
                "parts": [
                  {
                    "text": "**Formulating the Search Strategy**\n"
                  }
                ],
                "role": "MODEL",
                "planStepId": "123456789051"
              },
              "createTime": "2025-11-24T23:06:51.081693248Z"
            },
            {
              "createTime": "2025-11-24T23:06:53.884827627Z",
              "planStep": {
                "parts": [
                  {
                    "text": "**Searching for Information**\n"
                  }
                ],
                "role": "MODEL",
                "planStepId": "123456789051"
              }
            },
            {
              "createTime": "2025-11-24T23:06:55.663545003Z",
              "planStep": {
                "role": "MODEL",
                "parts": [
                  {
                    "text": "**Planning the Response Structure**\n"
                  }
                ],
                "planStepId": "123456789051"
              }
            },
            {
              "planStep": {
                "planStepId": "123456789051",
                "parts": [
                  {
                    "text": "Of course, I can provide a list of the common documents and information you'll need to file your personal income taxes. Having these ready can make the process much smoother.\n\n### **Documents for Filing Personal Taxes**\n\n| Category | Document/Information | Purpose |\n| :--- | :--- | :--- |"
                  }
                ],
                "role": "MODEL"
              },
              "createTime": "2025-11-24T23:06:55.687661122Z"
            },
            {
              "planStep": {
                "planStepId": "123456789051",
                "parts": [
                  {
                    "text": "\n| **Personal Information** | \u003cul\u003e\u003cli\u003eYour Social Security Number (SSN) or Individual Taxpayer Identification Number (ITIN)\u003c/li\u003e\u003cli\u003eSSNs or ITINs for your spouse and any dependents\u003c/li\u003e\u003c/ul\u003e | To identify you and your family members to the IRS. |\n| **Income Information** | \u003cul\u003e\u003cli\u003e**"
                  }
                ],
                "role": "MODEL"
              },
              "createTime": "2025-11-24T23:06:55.713426005Z"
            },
            {
              "planStep": {
                "role": "MODEL",
                "parts": [
                  {
                    "text": "W-2 forms** from all employers.\u003c/li\u003e\u003cli\u003e**1099 forms** such as 1099-NEC, 1099-DIV, 1099-INT, 1099-G.\u003c/li\u003e\u003cli\u003eRecords of any other income (business, rental, etc.).\u003c/li\u003e\u003c/ul\u003e | To"
                  }
                ],
                "planStepId": "123456789051"
              },
              "createTime": "2025-11-24T23:06:56.158732383Z"
            },
            {
              "createTime": "2025-11-24T23:06:56.700143436Z",
              "planStep": {
                "role": "MODEL",
                "parts": [
                  {
                    "text": " report all of your income from various sources. |\n| **Deductions & Credits** | \u003cul\u003e\u003cli\u003eReceipts for charitable donations.\u003c/li\u003e\u003cli\u003eMedical expense records.\u003c/li\u003e\u003cli\u003e**Form 1098** (mortgage interest) & **1098-T** (tuition).\u003c/li\u003e\u003cli\u003eChild"
                  }
                ],
                "planStepId": "123456789051"
              }
            },
            {
              "planStep": {
                "planStepId": "123456789051",
                "role": "MODEL",
                "parts": [
                  {
                    "text": "care expense records.\u003c/li\u003e\u003c/ul\u003e | To reduce your taxable income and take advantage of tax credits. |\n| **Other Documents** | \u003cul\u003e\u003cli\u003eLast year's tax return.\u003c/li\u003e\u003cli\u003eBank account and routing numbers.\u003c/li\u003e\u003c/ul\u003e | For reference and to receive a direct deposit refund or make a payment. |\n\n---\n\nThis"
                  }
                ]
              },
              "createTime": "2025-11-24T23:06:57.410549380Z"
            },
            {
              "planStep": {
                "planStepId": "123456789051",
                "parts": [
                  {
                    "text": " list covers the most common items, but your specific needs may vary depending on your financial situation. It's always a good idea to keep your tax-related documents organized throughout the year.\n\nIs there a specific type of income or deduction you would like to know more about?"
                  }
                ],
                "role": "MODEL"
              },
              "createTime": "2025-11-24T23:06:57.960883085Z"
            }
          ]
        }
      },
      "sessionInfo": {
        "session": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
        "queryId": "123456789057",
        "turnId": "123456789013_123456789072"
      },
      "assistToken": "1234567890123456789012345678901234567890"
    }
    

For more information on the fields and what is returned, see [Response body](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist#response-body).

**Note:** To continue the conversation in the same session, save the `session` value from the response and include it in your next query.

### Python

Before trying this sample, follow the Python setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Update these variables before running the sample.
    project_id = "YOUR_PROJECT_ID"
    location = "YOUR_LOCATION"
    engine_id = "YOUR_APP_ID"
    session = "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions/SESSION_ID" # From previous session
    query = "What is Gemini Enterprise?"
    
    
    def stream_assist_session_sample(
        project_id: str,
        location: str,
        engine_id: str,
        session: str,
        query: str,
    ):
        # For more information, refer to:
        # https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        client = discoveryengine.AssistantServiceClient(client_options=client_options)
    
        request = discoveryengine.StreamAssistRequest(
            name=client.assistant_path(
                project=project_id,
                location=location,
                collection="default_collection",
                engine=engine_id,
                assistant="default_assistant",
            ),
            session=session,
            query=discoveryengine.Query(text=query),
        )
    
        # Make the request
        stream = client.stream_assist(request=request)
    
        # Handle the response
        for response in stream:
            print(response.answer)
            # Get Session ID
            print(response.session_info.session)
    

## Upload a file and get search results (Preview)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To give the assistant more context, upload a file to a session and then query its content. Follow these steps:

  1. Upload a file to a session using the [`addContextFile`](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/addContextFile) method.

### REST
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/sessions/SESSION_ID:addContextFile" \
           -d '
         {
           "fileName": "FILE_NAME",
           "mimeType": "MIME_TYPE",
           "fileContents": "BASE64_ENCODED_FILE"
         }'
         

Replace the following:

     * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
       * `us` for the US multi-region
       * `eu` for the EU multi-region
       * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the multi-region of your data store: `global`, `us`, or `eu`
     * APP_ID: the unique identifier for the Gemini Enterprise app.
     * SESSION_ID: the ID of a session from a previous conversation or query.
     * FILE_NAME: the name of the file.
     * MIME_TYPE: the MIME type of the file, for example, `text/plain` or `application/pdf`. For more information on the different media types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml).
     * BASE64_ENCODED_FILE: the base64-encoded representation of the file.

#### Example command and result
    
    # Create a sample file to upload
    export FILE_NAME="my_test_file.txt"
    export FILE_PATH="/tmp/${FILE_NAME}"
    echo "This is a sample text file to upload for the Gemini Enterprise assistant." > "${FILE_PATH}"
    echo "It contains a few lines of text." >> "${FILE_PATH}"
    
    # Base64 encode the file content
    export BASE64_ENCODED_FILE=$(base64 -w 0 "${FILE_PATH}")
    
    
    
    * * *
    
    
    #Upload the file to the session using the curl command
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013:addContextFile" \
      -d '
    {
      "fileName": "my_test_file.txt",
      "mimeType": "text/plain",
      "fileContents": "'"$BASE64_ENCODED_FILE"'"
    }'
    
    
    * * *
    
    
    # Response
    
    {
      "session": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
      "fileId": "123456789012345",
      "tokenCount": "24"
    }
    
    
    

For more information on the fields and what is returned, see [Response body](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/addContextFile#response-body).

**Note:** To continue the conversation in the same session, save the `session` and the `fileId` values from the response and include them in your next query.

  2. Use the same session to ask a question about the file you uploaded using the [`streamAssist`](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/streamAssist) method.

### REST
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
           -d '
         {
           "session": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions/SESSION_ID",
           "fileIds": ["FILE_ID"],
           "query": {
             "text": "QUERY_TEXT_3"
           }
         }'
         
         

Replace the following:

     * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
       * `us` for the US multi-region
       * `eu` for the EU multi-region
       * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
     * PROJECT_ID: the ID of your Google Cloud project.
     * APP_ID: the unique identifier for the Gemini Enterprise app.
     * LOCATION: the multi-region of your data store: `global`, `us`, or `eu`
     * QUERY_TEXT_3: the search query text.
     * SESSION_ID: the ID of a session from a previous conversation or query.
     * FILE_ID: the ID of the file you uploaded to the assistant.

#### Example command and result
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant:streamAssist" \
      -d '
    {
      "session": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
      "fileIds": ["123456789012345"],
      "query": {
        "text": "Repeat the text in the file"
      }
    }'
    
    
    * * *
    
    
    {
      "answer": {
        "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013/assistAnswers/123456789065",
        "state": "SUCCEEDED",
        "replies": [
          {
            "groundedContent": {},
            "replyId": "123456789009"
          },
          {
            "groundedContent": {},
            "replyId": "717422098702389109"
          }
        ],
        "diagnosticInfo": {
          "plannerSteps": [
            {
              "createTime": "2025-11-26T03:56:30.270018719Z",
              "queryStep": {
                "parts": [
                  {
                    "text": "repeat the text in the file"
                  },
                  {}
                ]
              }
            },
            {
              "createTime": "2025-11-26T03:56:32.976071976Z",
              "planStep": {
                "role": "MODEL",
                "planStepId": "717422098702389109",
                "parts": [
                  {
                    "text": "**Addressing the Repetition**\n"
                  }
                ]
              }
            },
            {
              "createTime": "2025-11-26T03:56:35.390573666Z",
              "planStep": {
                "planStepId": "717422098702389109",
                "parts": [
                  {
                    "text": "**Identifying User Intent**\n"
                  }
                ],
                "role": "MODEL"
              }
            },
            {
              "createTime": "2025-11-26T03:56:37.586889807Z",
              "planStep": {
                "planStepId": "717422098702389109",
                "parts": [
                  {
                    "text": "**Analyzing the Repetition**\n"
                  }
                ],
                "role": "MODEL"
              }
            },
            {
              "createTime": "2025-11-26T03:56:37.611172643Z",
              "planStep": {
                "parts": [
                  {
                    "text": "Of course. The text in the file `my_test_file.txt` is:\n\nThis is a sample text file to upload for the Gemini Enterprise assistant.\nIt contains a few lines of text.\n\nIs there anything else I can assist you with?"
                  }
                ],
                "role": "MODEL",
                "planStepId": "717422098702389109"
              }
            }
          ]
        }
      },
      "sessionInfo": {
        "session": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions/8715627784376195363",
        "queryId": "2129985467851228910",
        "turnId": "8715627784376195363_2129985467851230549"
      },
      "assistToken": "NMwKDAjt9JnJBhCGypGkARIkNjkyMWQzZjktMDAwMC0yM2UyLWJlMjAtNTgyNDI5YTdhOTYw"
    }
    

For more information on the fields and what is returned, see [Response body](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist#response-body).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
