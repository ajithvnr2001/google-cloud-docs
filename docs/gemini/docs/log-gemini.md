---
url: https://docs.cloud.google.com/gemini/docs/log-gemini/
title: View Gemini Code Assist logs \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:44.630555+00:00
---

# View Gemini Code Assist logs  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/log-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  View Gemini Code Assist logs Stay organized with collections  Save and categorize content based on your preferences. 

Collecting Gemini Code Assist activity in Cloud Logging lets you audit developer prompts, model responses, and metadata logs such as telemetry data and accepted lines of code. You can query these log entries to evaluate assistant interactions across your organization. To track aggregated trends instead of raw logs, see [Monitor Gemini Code Assist usage](https://docs.cloud.google.com/gemini/docs/codeassist/generate-metrics).

Gemini Code Assist doesn't collect or send to Cloud Logging any other user interactions the user might have had with Gemini Code Assist, including written feedback. The collected data is sent to Cloud Logging for storage. You can review this data by searching for log entries with the resource type `cloudaicompanion.googleapis.com/Instance`.

**Note:** Google doesn't use prompts or responses as data to train its model, whether or not Gemini Code Assist logging is enabled. When Gemini Code Assist logging is enabled, Google _does_ log the data for use by your organization's system administrators.

This feature does not log prompts or responses within Gemini in Vertex AI. To enable logs for Gemini in Vertex AI, see [Enable Data Access audit logs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/enable-audit-logs).

Identity and Access Management (IAM) roles control the ability for a principal to access logs. You can grant predefined roles to principals, or you can create custom roles. For more information about required permissions, see [Access control](https://docs.cloud.google.com/logging/docs/access-control).

By default, Cloud Logging [encrypts customer content stored at rest](https://cloud.google.com/security/encryption/default-encryption/). Data stored in log buckets by Logging is encrypted using key-encryption keys, a process known as [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption). Access to your logging data requires access to those key-encryption keys, which Google manages for you without any actions on your part.

Your organization might have regulatory, compliance-related, or advanced encryption requirements that our default encryption at rest doesn't provide. To meet your organization's requirements, instead of Google managing the encryption keys that protect your data, you can manage your keys.

For specific information about customer-managed encryption keys (CMEK) usage, including advantages, and limitations, see [Customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek).

## Limitations

  * Gemini Code Assist log data recording is limited to user interactions with Gemini Code Assist within an IDE.

  * By default, Gemini Code Assist logs are collected on a per-project basis. For instructions on how to configure a centralized project to collect logs from multiple projects, see [Set up multi-project logging](https://docs.cloud.google.com/gemini/docs/configure-logging#multi-project-logging).




## Before you begin

  * To get the permissions that you need to view Gemini Code Assist logs , ask your administrator to grant you the [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Review [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing) and [Gemini Code Assist pricing](https://cloud.google.com/products/gemini/pricing).

  * [Enable Gemini Code Assist logging](https://docs.cloud.google.com/gemini/docs/configure-logging).




## View Gemini Code Assist user logs and metadata logs

To view Gemini Code Assist user logs and metadata logs, do one of the following:

###  Console 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the toolbar, select a Google Cloud console project.
  3. In the toolbar, expand the **All resources** menu and select the resource **Cloud AI Companion Instance**.



###  gcloud 

Run the following command:
    
    
    gcloud logging read "resource.type=cloudaicompanion.googleapis.com/Instance" --project PROJECT_ID  --limit 3
    

Replace `PROJECT_ID` with the ID of the project whose Gemini Code Assist logs you want to view.

###  API 

  1. Create a JSON file that contains the following information:
         
         {
             "resourceNames": [
               "projects/PROJECT_ID"
             ],
             "pageSize": 5,
             "filter": "resource.type: cloudaicompanion.googleapis.com/Instance"
           }
         

Replace `PROJECT_ID` with the ID of the project whose Gemini Code Assist logs you want to view.

  2. Obtain an [authentication token](https://docs.cloud.google.com/docs/authentication/rest):
         
         TOKEN=$(gcloud auth print-access-token)
         

  3. Use [`cURL`](http://curl.haxx.se/) to call the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           "https://logging.googleapis.com/v2/entries:list"

Replace `JSON_FILE_NAME` with the path for the JSON file that you created in the preceding step.

For more information on authentication, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest).

The response returns a set of log entries.




### Gemini Code Assist logs

A [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) is the basic unit of data in Cloud Logging. The following sections provide lists of fields found in the `LogEntry` for a Gemini Code Assist platform event, such as user requests and Gemini Code Assist responses.

#### User requests

The following table shows a list of fields found in a user request log entry:

Field | Values and notes  
---|---  
`LogEntry.resource.type` | Gemini Code Assist [resource type](https://docs.cloud.google.com/logging/docs/api/v2/resource-list): `cloudaicompanion.googleapis.com/Instance`.  
`LogEntry.resource.labels.resource_container` | Unique ID of the Resource Container where Gemini Code Assist was used.  
`LogEntry.resource.labels.location` | Location where Gemini Code Assist was used.  
`LogEntry.resource.labels.instance_id` | Unique ID of the resource where Gemini Code Assist was used.  
`LogEntry.labels.method` | Can be one of the following, depending on what invoked `logEntry`:  
  
`CompleteTask`: for example, a chat request from [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini#chat).  
  
`GenerateCode`: for example, a request to generate code, such as with a [code transformation](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini#generate_code_with_prompts) request within Gemini Code Assist.  
  
`CompleteCode`: for example, a request to complete code when working in the IDE, such as with [inline suggestions](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini#get_code_completions) within Gemini Code Assist.  
`LogEntry.labels.product` | Name of the service the log applies to. Logs relevant for Gemini Code Assist use the product value `code_assist`. If the log is relevant for Gemini Cloud Assist, then this value is `cloud_assist`. Otherwise, this value is `unknown`.  
`LogEntry.labels.request_id` | A unique identifier to correlate a request to a response log entry.  
`LogEntry.labels.user_id` | The identifier of the user that initiated this request.  
`LogEntry.jsonPayload` | The payload of the log entry.  
`LogEntry.logName` | Identifies the log.  
  
The following sample shows an example log entry for a chat prompt event:
    
    
    {
      "insertId": "654581e30003b19e340bbd96",
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
            instance_id: "default"
            location: "global"
            resource_container: "my-project-id"
         }
      },
      "timestamp": "2023-11-03T23:27:31.242078Z",
      "labels": {
        "product": "code_assist",
        "request_id": "4ea1e265-ea5d-4d11-b3c8-39bad9c96326"
        "user_id": "user@company.com"
      },
      "jsonPayload" : {
        @type: "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.RequestLog"
        "taskCompletionRequest":
          input: {
            messages: [{
              author: "USER"
              content: "What are some best practices to save cost on my Google Cloud bill?"
            }]
            preamble: ""
          }
      }
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Frequest",
      "receiveTimestamp": "2023-11-03T23:27:31.255648319Z"
      "severity": "INFO"
    }
    

The following sample shows an example `RequestLog` entry for automatic [inline code suggestion](https://docs.cloud.google.com/workstations/docs/write-code-gemini#get_inline_suggestions_while_you_code) prompts and [prompting Gemini Code Assist in a code file](https://docs.cloud.google.com/workstations/docs/write-code-gemini#prompt-gemini-in-code-file).

Prompt data for inline code suggestions uses the `codeCompletionRequest` object (as shown in the following example), while manually-triggered generation uses `codeGenerationRequest`.
    
    
    {
      "insertId": "654581e30003b19e340bbd96",
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
            instance_id: "default"
            location: "global"
            resource_container: "my-project-id"
         }
      },
      "timestamp": "2023-11-03T23:27:31.242078Z",
      "labels": {
        "product": "code_assist",
        "request_id": "4ea1e265-ea5d-4d11-b3c8-39bad9c96326"
        "user_id": "user@company.com"
      },
      "jsonPayload" : {
        @type: "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.RequestLog"
        "codeCompletionRequest": {
          "input_data_context": {
            "additional_context": {
              "files": [
                {
                  "language": "go",
                  "path": "{/path/to/../current-file.go",
                  "segments": [
                    {
                      "content": "...Prefix Text..."
                    },
                    {
                      "content": "...Suffix Text..."
                    }
                  ],
                  "state": ["EDITED"]
                },
                {
                  "language": "go",
                  "path": "/path/to/../recent-file.go",
                  "segments": [
                    {
                      "content": "...File Text..."
                    }
                  ],
                  "state": ["RECENTLY_OPENED"]
                }
              ]
            }
          }
        }
      }
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Frequest",
      "receiveTimestamp": "2023-11-03T23:27:31.255648319Z"
      "severity": "INFO"
    }
    

#### Agent interaction logs

Some interactions with Gemini can generate multiple log entries (request, response, and metadata) for a single user action. Examples of such interactions include the following:

  * An agent performing a task that involves tool use (for instance, the model invoking internal functions like `read_file` or `replace`, as shown in the log examples).
  * An agent interacting with other agents.



##### Request log entry

The following sample shows an example log entry for a request that initiates an agent interaction:
    
    
    {
      "insertId": "qe9xxub2r",
      "jsonPayload": {
        "taskCompletionRequest": {
          "input": {
            "messages": [
              {
                "author": "USER",
                "content": "hi can you add one test here\nCurrent File Path:\n```cpp\n/usr/local/google/home/pdec/test.cpp\n```\n\n"
              }
            ],
            "preamble": ""
          }
        },
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.RequestLog"
      },
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
          "resource_container": "my-project-id",
          "instance_id": "default",
          "location": "global"
        }
      },
      "timestamp": "2025-10-08T10:09:52.225165428Z",
      "severity": "INFO",
      "labels": {
        "request_id": "e60facb1485b17b7",
        "client_version": "unknown",
        "product": "code_assist",
        "method": "CompleteTask",
        "user_id": "user@company.com",
        "client_name": "cloudcode_cli"
      },
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Frequest",
      "receiveTimestamp": "2025-10-08T10:09:52.581787548Z"
    }
    

##### Response log entry

The following sample shows an example response log entry from an agent interaction that includes multiple messages:
    
    
    {
      "insertId": "qe9xxub2t",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.ResponseLog",
        "taskCompletionResponse": {
          "output": {
            "messages": [
              {
                "content": "**Reading File Contents**\n\nI'm currently focused on reading the contents of `/usr/local/google/home/pdec/test.cpp`. This will inform what kind of test needs to be written and how it should be structured.\n\n\n",
                "author": "MODEL"
              },
              {
                "author": "MODEL",
                "content": "**File Inspection Begins**\n\nI've initiated the process of reading the test file. My immediate goal is to grasp its existing structure and identify the testing framework, if one exists. This will directly influence the design of the new test case I'll be adding.\n\n\n"
              },
              {
                "author": "MODEL",
                "content": "Of course. What is the test about? I'll read the file to understand the context."
              },
              {
                "content": "read_file({\"absolute_path\":\"/usr/local/google/home/pdec/test.cpp\"})",
                "author": "MODEL"
              }
            ]
          }
        }
      },
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
          "resource_container": "my-project-id",
          "instance_id": "default",
          "location": "global"
        }
      },
      "timestamp": "2025-10-08T10:09:52.227354297Z",
      "severity": "INFO",
      "labels": {
        "product": "code_assist",
        "request_id": "e60facb1485b17b7",
        "user_id": "user@company.com",
        "client_version": "unknown",
        "method": "CompleteTask",
        "client_name": "cloudcode_cli"
      },
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fresponse",
      "receiveTimestamp": "2025-10-08T10:09:52.581787548Z"
    }
    

##### Metadata log entry

The following sample shows an example metadata log entry from an agent interaction:
    
    
    {
      "insertId": "qe9xxub2s",
      "jsonPayload": {
        "apiRequest": {},
        "clientName": "cloudcode_cli",
        "requestId": "e60facb1485b17b7",
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.MetadataLog",
        "clientVersion": "unknown"
      },
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
          "location": "global",
          "instance_id": "default",
          "resource_container": "my-project-id"
        }
      },
      "timestamp": "2025-10-08T10:09:52.226420727Z",
      "severity": "INFO",
      "labels": {
        "method": "CompleteTask",
        "product": "code_assist",
        "user_id": "user@company.com"
      },
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fmetadata",
      "receiveTimestamp": "2025-10-08T10:09:52.581787548Z"
    }
    

The following samples show another example of log entries for an agent interaction, with request ID `4b66a582bad9cf2c`:

**Request log entry**
    
    
    {
      "insertId": "4qvt8nb2k",
      "jsonPayload": {
        "taskCompletionRequest": {
          "input": {
            "messages": [
              {
                "author": "USER",
                "content": "FunctionResponse{name: read_file, response: {\"output\":\"#include <iostream>\\n\\n// Function to calculate the greatest common divisor (GCD) of two numbers.\\nint gcd(int a, int b) {\\n    if (b == 0) {\\n        return a;\\n    }\\n    return gcd(b, a % b);\\n}\\n\\n// Function to calculate the least common multiple (LCM) of two numbers.\\nint lcm(int a, int b) {\\n    return (a * b) / gcd(a, b);\\n}\\n\\n// Function to check if a number is prime.\\nint is_prime(int a) {\\n    if (a < 2) {\\n        return 0;\\n    }\\n    for (int i = 2; i * i <= a; ++i) {\\n        if (a % i == 0) {\\n            return 0;\\n        }\\n    }\\n    return 1;\\n}\\n\\n// Function for extended Euclidean algorithm.\\nint extended_gcd(int a, int b, int &x, int &y) {\\n    if (b == 0) {\\n        x = 1;\\n        y = 0;\\n        return a;\\n    }\\n    int x1, y1;\\n    int d = extended_gcd(b, a % b, x1, y1);\\n    x = y1;\\n    y = x1 - (a / b) * y1;\\n    return d;\\n}\\n\\n// Test function\\nvoid run_tests() {\\n    // Test gcd\\n    if (gcd(10, 15) == 5) {\\n        std::cout << \\\"gcd(10, 15) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"gcd(10, 15) failed\\\" << std::endl;\\n    }\\n\\n    // Test lcm\\n    if (lcm(10, 15) == 30) {\\n        std::cout << \\\"lcm(10, 15) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"lcm(10, 15) failed\\\" << std::endl;\\n    }\\n\\n    // Test is_prime\\n    if (is_prime(7) == 1) {\\n        std::cout << \\\"is_prime(7) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"is_prime(7) failed\\\" << std::endl;\\n    }\\n    if (is_prime(10) == 0) {\\n        std::cout << \\\"is_prime(10) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"is_prime(10) failed\\\" << std::endl;\\n    }\\n\\n    // Test extended_gcd\\n    int x, y;\\n    int g = extended_gcd(35, 15, x, y);\\n    if (g == 5 && 35 * x + 15 * y == g) {\\n        std::cout << \\\"extended_gcd(35, 15) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"extended_gcd(35, 15) failed\\\" << std::endl;\\n    }\\n\\n    // Test is_prime with 1\\n    if (is_prime(1) == 0) {\\n        std::cout << \\\"is_prime(1) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"is_prime(1) failed\\\" << std::endl;\\n    }\\n\\n    // Test is_prime with 9\\n    if (is_prime(9) == 0) {\\n        std::cout << \\\"is_prime(9) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"is_prime(9) failed\\\" << std::endl;\\n    }\\n\\n    // Test is_prime with 13\\n    if (is_prime(13) == 1) {\\n        std::cout << \\\"is_prime(13) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"is_prime(13) failed\\\" << std::endl;\\n    }\\n\\n    // Test lcm with 7 and 9\\n    if (lcm(7, 9) == 63) {\\n        std::cout << \\\"lcm(7, 9) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"lcm(7, 9) failed\\\" << std::endl;\\n    }\\n\\n    // Test gcd with 12 and 18\\n    if (gcd(12, 18) == 6) {\\n        std::cout << \\\"gcd(12, 18) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"gcd(12, 18) failed\\\" << std::endl;\\n    }\\n\\n    // Test gcd with two primes\\n    if (gcd(7, 13) == 1) {\\n        std::cout << \\\"gcd(7, 13) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"gcd(7, 13) failed\\\" << std::endl;\\n    }\\n\\n    // Test is_prime with 97\\n    if (is_prime(97) == 1) {\\n        std::cout << \\\"is_prime(97) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"is_prime(97) failed\\\" << std::endl;\\n    }\\n\\n    // Test extended_gcd with 48 and 18\\n    int x2, y2;\\n    int g2 = extended_gcd(48, 18, x2, y2);\\n    if (g2 == 6 && 48 * x2 + 18 * y2 == g2) {\\n        std::cout << \\\"extended_gcd(48, 18) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"extended_gcd(48, 18) failed\\\" << std::endl;\\n    }\\n\\n    // Test gcd with 27 and 18\\n    if (gcd(27, 18) == 9) {\\n        std::cout << \\\"gcd(27, 18) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"gcd(27, 18) failed\\\" << std::endl;\\n    }\\n    // test 999 and 123\\n    if (gcd(999, 123) == 3) {\\n        std::cout << \\\"gcd(999, 123) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"gcd(999, 123) failed\\\" << std::endl;\\n    }\\n    \\n    \\n}\\n\\nint main() {\\n    run_tests();\\n    return 0;\\n}\"}}"
              }
            ],
            "preamble": ""
          }
        },
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.RequestLog"
      },
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
          "resource_container": "my-project-id",
          "instance_id": "default",
          "location": "global"
        }
      },
      "timestamp": "2025-10-08T10:10:03.457717366Z",
      "severity": "INFO",
      "labels": {
        "request_id": "4b66a582bad9cf2c",
        "method": "CompleteTask",
        "client_version": "unknown",
        "product": "code_assist",
        "client_name": "cloudcode_cli",
        "user_id": "user@company.com"
      },
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Frequest",
      "receiveTimestamp": "2025-10-08T10:10:03.606059154Z"
    }
    

**Response log entry**
    
    
    {
      "insertId": "4qvt8nb2m",
      "jsonPayload": {
        "taskCompletionResponse": {
          "output": {
            "messages": [
              {
                "author": "MODEL",
                "content": "**Testing the functions**\\n\\nI'm focusing on adding a new test case to `test.cpp`.  The existing `run_tests` function is a great starting point. I'm considering which function to test further – maybe `extended_gcd`? I'll review the current tests for that function and then devise a new test scenario to add.\\n\\n\\n"
              },
              {
                "author": "MODEL",
                "content": "**Evaluating LCM Test**\\n\\nI've finalized the new test case for the `lcm` function within the `test.cpp` file.  I'm adding a test for `lcm(12, 18)` to confirm the result is 36. I plan to use the `replace` command to inject this new test directly before the closing brace of the `run_tests` function.  I've identified a unique line in `test.cpp` as the anchor for replacement.\\n\\n\\n"
              },
              {
                "author": "MODEL",
                "content": "**Inserting the new test**\\n\\nI've created a test case for `lcm(12, 18)`, confirming the expected result of 36. To implement this, I'm targeting the `run_tests` function.  I'll use the `replace` command and will search the end of the `run_tests` function to inject the new test, right before the closing brace.  I'm ready to implement this and confirm that it passes.\\n\\n\\n"
              },
              {
                "author": "MODEL",
                "content": "I've reviewed the file. I'll add a test case for the `lcm` function with inputs 12 and 18."
              },
              {
                "content": "replace({\"file_path\":\"/usr/local/google/home/pdec/test.cpp\",\"instruction\":\"add a test for the lcm function with 12 and 18\",\"new_string\":\"    // test 999 and 123\\n    if (gcd(999, 123) == 3) {\\n        std::cout << \\\"gcd(999, 123) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"gcd(999, 123) failed\\\" << std::endl;\\n    }\\n    \\n    // Test lcm with 12 and 18\\n    if (lcm(12, 18) == 36) {\\n        std::cout << \\\"lcm(12, 18) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"lcm(12, 18) failed\\\" << std::endl;\\n    }\\n    \\n}\",\"old_string\":\"    // test 999 and 123\\n    if (gcd(999, 123) == 3) {\\n        std::cout << \\\"gcd(999, 123) passed\\\" << std::endl;\\n    } else {\\n        std::cout << \\\"gcd(999, 123) failed\\\" << std::endl;\\n    }\\n    \\n    \\n}\"})",
                "author": "MODEL"
              }
            ]
          }
        },
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.ResponseLog"
      },
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
          "location": "global",
          "resource_container": "my-project-id",
          "instance_id": "default"
        }
      },
      "timestamp": "2025-10-08T10:10:03.461137399Z",
      "severity": "INFO",
      "labels": {
        "client_name": "cloudcode_cli",
        "client_version": "unknown",
        "method": "CompleteTask",
        "request_id": "4b66a582bad9cf2c",
        "product": "code_assist",
        "user_id": "user@company.com"
      },
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fresponse",
      "receiveTimestamp": "2025-10-08T10:10:03.606059154Z"
    }
    

**Metadata log entry**
    
    
    {
      "insertId": "4qvt8nb2l",
      "jsonPayload": {
        "clientVersion": "unknown",
        "apiRequest": {},
        "clientName": "cloudcode_cli",
        "requestId": "4b66a582bad9cf2c",
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.MetadataLog"
      },
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
          "resource_container": "my-project-id",
          "location": "global",
          "instance_id": "default"
        }
      },
      "timestamp": "2025-10-08T10:10:03.459902984Z",
      "severity": "INFO",
      "labels": {
        "product": "code_assist",
        "user_id": "user@company.com",
        "method": "CompleteTask"
      },
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fmetadata",
      "receiveTimestamp": "2025-10-08T10:10:03.606059154Z"
    }
    

#### Gemini Code Assist responses

The following table shows Gemini Code Assist response fields and descriptions:

Field | Values and notes  
---|---  
`LogEntry.resource.type` | Gemini Code Assist [resource type](https://docs.cloud.google.com/monitoring/api/resources): `cloudaicompanion.googleapis.com/Instance`.  
`LogEntry.resource.labels.resource_container` | Unique ID of the Resource Container where Gemini Code Assist was used.  
`LogEntry.resource.labels.location` | Location where Gemini Code Assist was used.  
`LogEntry.resource.labels.instance_id` | Unique ID of the resource where Gemini Code Assist was used.  
`LogEntry.labels.method` | Can be one of the following, depending on what invoked `logEntry`:  
  
`CompleteTask`: for example, a chat request from [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini#chat).  
  
`GenerateCode`: for example, a request to generate code, such as with a [code transformation](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini#generate_code_with_prompts) request within Gemini Code Assist.  
  
`CompleteCode`: for example, a request to complete code when working in the IDE, such as with [inline suggestions](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini#get_code_completions) within Gemini Code Assist.  
`LogEntry.labels.product` | Name of the service the log applies to. Logs relevant for Gemini Code Assist use the product value `code_assist`. If the log is relevant for Gemini Cloud Assist, then this value is `cloud_assist`. Otherwise, this value is `unknown`.  
`LogEntry.labels.request_id` | A unique identifier to correlate a request to a response log entry.  
`LogEntry.labels.user_id` | The identifier of the user that initiated this request.  
`LogEntry.jsonPayload` | The payload of the log entry. Any source citations used to generate the response are included in this object as `attribution_context`.  
`LogEntry.logName` | Identifies the log.  
  
### Gemini Code Assist metadata logs

For the metadata logs to be generated, the _Gemini Code Assist extension_ telemetry setting must be enabled for both VS Code and IntelliJ extensions.

Gemini Code Assist metadata logs follow the same structure as Gemini Code Assist logs but specify different fields. The following table shows a list of fields found in a user request log entry:

Field | Values and notes  
---|---  
`LogEntry.@type` | Gemini Code Assist metadata [resource type](https://docs.cloud.google.com/logging/docs/api/v2/resource-list): `type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.MetadataLog`.  
`LogEntry.labels.method` | For metadata logs, this label value is `Export.Metrics`.  
`LogEntry.labels.product` | Name of the service the log applies to. Logs relevant for Gemini Code Assist use the product value `code_assist`. If the log is relevant for Gemini Cloud Assist, then this value is `cloud_assist`. Otherwise, this value is `unknown`.  
`LogEntry.labels.user_id` | The identifier of the user that initiated this request.  
`LogEntry.jsonPayload` | Indicates either a `codeExposure` event or `code.Acceptance` event. A `codeExposure` event indicates an exposure of a code suggestion to a user. A `code.Acceptance` event indicates there was some acceptance event by the user, such as typeover, tab, or full acceptance.  
`LogEntry.jsonPayload.clientName` | The IDE name, such as `CloudCodeVscode`.  
`LogEntry.jsonPayload.clientVersion` | The IDE version number.  
`LogEntry.jsonPayload.codeAcceptance` | For VS Code and IntelliJ IDEs only, indicates there was some acceptance event by the user, such as typeover, tab, or full acceptance. Also includes the following fields:

  * `linesCount`: the total number of lines of code accepted by the user.
  * `commentLinesCount`: the number of comment lines in the code accepted by the user. This property only appears if Gemini Code Assist is able to determine how many of the accepted lines are comment lines.
  * `originalRequestId`: an identifier linking a `codeExposure` event to zero or more `codeAcceptance` events. This can be used to calculate acceptance rate and lines of code accepted measures.
  * `programmingLanguage`: programming language of the accepted code, such as `python`.

  
`LogEntry.jsonPayload.codeExposure` | For VS Code and IntelliJ IDEs only, indicates there was exposure of a code suggestion to a user. Also includes the following fields:

  * `programmingLanguage`: programming language of the exposure, such as `python`.
  * `originalRequestId`: an identifier linking a `codeExposure` event to zero or more `codeAcceptance` events. This can be used to calculate acceptance rate and lines of code accepted measures.

  
`LogEntry.jsonPayload.chatExposure` | Indicates there was exposure of a chat response to a user. Also includes the following fields:

  * `originalRequestId`: an identifier linking a `chatExposure` event to zero or more `chatAcceptance` events. This can be used to calculate chat acceptance rate and lines of chat accepted measures.
  * `is_agentic`: An identifier that indicates whether chatExposure comes from Agent Mode. This can be used to distinguish Agent Mode and non-Agent Mode chat acceptance rate and lines of code accepted measures.

  
`LogEntry.jsonPayload.chatAcceptance` | Indicates there was some acceptance event by the user on the code blocks in the chat response. Also includes the following fields:

  * `interactionType`: the type of interaction the user had with the code block, such as `ACCEPT_CODE_BLOCK`.
  * `programmingLanguage`: programming language of the accepted code, such as `python`.
  * `linesCount`: the total number of lines of code accepted by the user.
  * `originalRequestId`: an identifier linking a `chatExposure` event to zero or more `chatAcceptance` events.
  * `is_agentic`: an identifier whether chatAcceptance comes from Agent Mode. This can be used to distinguish Agent Mode and non-Agent Mode chat acceptance rate and lines of code accepted measures.

  
  
The following sample shows an example `codeExposure` log entry:
    
    
    {
      insertId: "whfrqgc1gj"
      jsonPayload: {
        @type: "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.MetadataLog"
        clientName: "CloudCodeVscode"
        clientVersion: "1.93.1"
        codeExposure: {
          originalRequestId: "cac019824a0b25ba"
          programmingLanguage: "python"
        }
      requestId: "0c5178fe-446f-4ab6-b996-520dec100cf8"
      }
      labels: {
        method: "Export.Metrics"
        product: "code_assist"
        user_id: "user@company.com"
      }
      logName: "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fmetadata"
      receiveTimestamp: "2025-02-03T23:34:35.662837985Z"
      resource: {
        labels: {
          instance_id: "default"
          location: "global"
          resource_container: "my-project-id"
        }
      type: "cloudaicompanion.googleapis.com/Instance"
      }
      severity: "INFO"
      timestamp: "2025-02-03T23:34:35.021564463Z"
    }
    

The following sample shows an example `codeAcceptance` log entry:
    
    
    {
      insertId: "whfrqgc1gk"
      jsonPayload: {
        @type: "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.MetadataLog"
        clientName: "CloudCodeVscode"
        clientVersion: "1.93.1"
        codeAcceptance: {
          linesCount: 2
          originalRequestId: "cac019824a0b25ba"
          programmingLanguage: "python"
        }
        requestId: "ddf11040-c315-452e-b7cd-928c3f97984e"
      }
      labels: {
        method: "Export.Metrics"
        product: "code_assist"
        user_id: "user@company.com"
      }
      logName: "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fmetadata"
      receiveTimestamp: "2025-02-03T23:34:37.632662272Z"
      resource: {
        labels: {
          instance_id: "default"
          location: "global"
          resource_container: "my-project-id"
        }
        type: "cloudaicompanion.googleapis.com/Instance"
      }
      severity: "INFO"
      timestamp: "2025-02-03T23:34:36.778692483Z"
    } 
    

The following sample shows an example `chatAcceptance` log entry:
    
    
    {
      "insertId": "1oru1grbow",
      "jsonPayload": {
        "clientVersion": "1.103.2",
        "requestId": "32a0b0b8c967d8e8",
        "clientName": "CloudCodeVscode",
        "chatAcceptance": {
          "interactionType": "ACCEPT_CODE_BLOCK",
          "programmingLanguage": "go",
          "linesCount": "15",
          "originalRequestId": "75f7c41e63162567"
        },
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.MetadataLog"
      },
      "resource": {
        "type": "cloudaicompanion.googleapis.com/Instance",
        "labels": {
          "resource_container": "my-project-id",
          "instance_id": "default",
          "location": "global"
        }
      },
      "timestamp": "2025-08-25T09:34:01.240377123Z",
      "severity": "INFO",
      "labels": {
        "product": "code_assist",
        "method": "Export.Metrics",
        "user_id": "user@company.com"
      },
      "logName": "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fmetadata",
      "receiveTimestamp": "2025-08-25T09:34:01.704925625Z"
    }
    

The following sample shows an example `chatExposure` log entry:
    
    
    {
      insertId: "3diaj2c208"
      jsonPayload: {
        @type: "type.googleapis.com/google.cloud.cloudaicompanion.logging.v1.MetadataLog"
        clientName: "CloudCodeVscode"
        clientVersion: "1.93.1"
        chatExposure: {
          originalRequestId: "cac019824a0b25ba"
        }
      requestId: "0c5178fe-446f-4ab6-b996-520dec100cf8"
      }
      labels: {
        method: "Export.Metrics"
        product: "code_assist"
        user_id: "user@company.com"
      }
      logName: "projects/my-project-id/logs/cloudaicompanion.googleapis.com%2Fmetadata"
      receiveTimestamp: "2025-02-03T23:34:35.662837985Z"
      resource: {
        labels: {
          instance_id: "default"
          location: "global"
          resource_container: "my-project-id"
        }
      type: "cloudaicompanion.googleapis.com/Instance"
      }
      severity: "INFO"
      timestamp: "2025-02-03T23:34:35.021564463Z"
    }
    

### Calculate acceptance rate

The following sections describe how to calculate the code suggestion acceptance rate, the chat response acceptance rate, and the total combined acceptance rate using Gemini Code Assist metadata logs.

#### Calculate code acceptance rate

To calculate the code acceptance rate using Gemini Code Assist metadata logs, find the total number of unique IDs from events with `codeAcceptance.originalRequestId` and divide it by the total number of unique IDs from events with `codeExposure.originalRequestId`.

You can further refine this calculation by programming language and by user using the respective metadata log event fields.

#### Calculate chat acceptance rate

To calculate the chat acceptance rate using Gemini Code Assist metadata logs, find the total number of unique IDs from events with `chatAcceptance.originalRequestId` and divide it by the total number of unique IDs from events with `chatExposure.originalRequestId`.

You can further refine this calculation by programming language and by user using the respective metadata log event fields.

#### Calculate total acceptance rate

To calculate the total acceptance rate using Gemini Code Assist metadata logs, find the total number of accepted events and divide that by the total number of exposure events:

_Total acceptance rate = Total accepted events ÷ Total exposure events_

  * **Total accepted events** : the total number of unique IDs from events with `codeAcceptance.originalRequestId` plus the total number of unique IDs from events with `chatAcceptance.originalRequestId`.
  * **Total exposure events** : the total number of unique IDs from events with `codeExposure.originalRequestId` plus the total number of unique IDs from events with `chatExposure.originalRequestId`.



This formula provides an acceptance rate that reflects the overall probability of any suggestion being accepted across all Gemini Code Assist features.

### Calculate lines of code accepted

The following sections describe how to calculate the number of lines of code accepted from code suggestions, the number of lines of code accepted from chat, and the total lines of code accepted using Gemini Code Assist metadata logs.

#### Calculate lines of code accepted

To calculate lines of code accepted, find the maximum value for `codeAcceptance.linesCount` for each unique `codeAcceptance.originalRequestId`. Then, sum these maximum values to calculate the total lines of code accepted.

You can further refine this calculation by programming language and by user using the respective metadata log event fields.

#### Calculate lines of code accepted from chat

To calculate lines of code accepted from chat, find the value of the `chatAcceptance.linesCount` field for each unique `chatAcceptance.originalRequestId`. Then, sum these maximum values to calculate the total lines of chat accepted.

#### Calculate total lines of code accepted

To calculate the total lines accepted using Gemini Code Assist metadata logs, add the lines of code accepted and lines of code accepted from chat.

## What's next

  * Learn how to [view, analyze, and monitor your logs in Google Cloud](https://docs.cloud.google.com/logging/docs/overview).
  * Learn more about [monitoring usage of Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/monitor-gemini).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
