---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-pagination-tailing/
title: Pagination and tailing \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:50:21.428545+00:00
---

# Pagination and tailing  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-pagination-tailing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Pagination and tailing Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use pagination and tailing when calling the endpoints of the [manager API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api).

## Pagination

Pagination is supported for most endpoints of the manager API. For exceptions, see Tailing an endpoint for updated records.

### Set the page size

By default, manager API endpoints return pages containing 100 records. You can change this number using the `per` query parameter.

To set the pages size, use the following endpoint:
    
    
    /manager/api/v1/agents?per=50
    

This sets the page size to 50 records.

### Request a specific page

You can request a specific page of records using the `page` query parameter.

To request a specific page, use the following endpoint:
    
    
    /manager/api/v1/agents?page=2
    

This returns the second page of records

### Get all available records

By default, the manager API returns 100 records in a response page, although you can change the number of records in a page by setting the page size. For the endpoints that support pagination, the response header includes the total number of records available. If that number exceeds your page size, you need to call the API multiple times to get all of the records. The manager API doesn't explicitly indicate that there are additional records to return.

To get all available records, do the following:

  1. Call a manager API endpoint that supports pagination. For more information, see Pagination. The response header indicates how many records there are to return.

  2. Compare the number of records to return with your page size. If the number of records to return is less than your page size, all of the records have been returned. Otherwise continue to the next step.

  3. Call the endpoint again, specifying the next page of records. For more information, see Request a specific page. Repeat this step until all of you records are returned.




## Tailing an endpoint for updated records

Google recommends against using pagination for the [call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-call), [chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-chat), and [agent activity](https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-agent-activity) API endpoints because we can't guarantee optimal results. Instead, we recommend tailing these API endpoints for updated records. Tailing an API endpoint means continuously calling it to get records that are new or updated since your last request.

### Tail the Calls API endpoint

Whenever a calls record is modified, its `updated_at` timestamp is updated. You can use the timestamp to specify the call records that you want to retrieve when calling the Calls API endpoint.

To tail the Calls API endpoint every 60 minutes, follow these steps:

  1. Make a request to the Calls API endpoint (`/manager/api/v1/calls`), specifying the following query parameters:

     * `updated_at[from]`. Specify that you want records that were updated on or after this time.

     * `sort_column`. Specify the field to sort the records by.

     * `sort_direction`. Specify the sort direction of the records in the response.

The following is an example Bash script that uses the `curl` command:
    
    # 1. Define your environment variables (usually set in your shell or .env file)
    export API_HOSTNAME="ccaip-host.uc1.ccaiplatform.com/"
    export API_USER="ccaip-host"
    export API_PASS="CCAI Platform API Key"
    
    # 2. Calculate the timestamp for 60 minutes ago in ISO 8601 format (UTC)
    # For macOS (BSD date):
    # TIMESTAMP=$(date -v-60M -u +"%Y-%m-%dT%H:%M:%SZ")
    # For Linux (GNU date):
    TIMESTAMP=$(date --date='60 minutes ago' -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # 3. Execute the curl command
    # -u handles the Base64 encoding for Basic Auth automatically
    curl -g -u "${API_USER}:${API_PASS}" \
    "https://${API_HOSTNAME}/manager/api/v1/calls?updated_at[from]=${TIMESTAMP}&sort_column=updated_at&sort_direction=asc" | jq
    

The Calls API returns a response similar to the following:
    
    [
        {
          "id": 100,
          ...
          "updated_at": "2025-01-01T00:00:00Z"
        },
        {
          "id": 98,
          ...
          "updated_at": "2025-01-02T00:00:00Z"
        },
        {
          "id": 150,
          ...
          "updated_at": "2025-01-03T00:00:00Z"
        }
      ]
    

Response objects updated on or after the timestamp you specified are returned, sorted by date, in ascending order. Use the `updated_at` timestamp from the last object in this response for the timestamp in your next call to the endpoint.

  2. Call the Call API endpoint 60 minutes later. The updated Call records since your last request are returned.

  3. Repeat the previous step to continue tailing the endpoint.




### Tail the Chats API endpoint

Whenever a chat record is modified, its `updated_at` timestamp is updated. You can use the timestamp to specify the chat records that you want to retrieve when calling the Chats API endpoint.

To tail the Chats API endpoint every 60 minutes, follow these steps:

  1. Make a request to the Chats API endpoint (`/manager/api/v1/chats`), specifying the following query parameters:

     * `updated_at[from]`. Specify that you want records that were updated on or after this time.

     * `sort_column`. Specify the field to sort the records by.

     * `sort_direction`. Specify the sort direction of the records in the response.

The following is an example Bash script that uses the `curl` command:
    
    # 1. Define your environment variables (usually set in your shell or .env file)
    export API_HOSTNAME="ccaip-host.uc1.ccaiplatform.com/"
    export API_USER="ccaip-host"
    export API_PASS="CCAI Platform API Key"
    
    # 2. Calculate the timestamp for 60 minutes ago in ISO 8601 format (UTC)
    # For macOS (BSD date):
    # TIMESTAMP=$(date -v-60M -u +"%Y-%m-%dT%H:%M:%SZ")
    # For Linux (GNU date):
    TIMESTAMP=$(date --date='60 minutes ago' -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # 3.. Execute the curl command
    # -u handles the Base64 encoding for Basic Auth automatically
    curl -g -u "${API_USER}:${API_PASS}" \
    "https://${API_HOSTNAME}/manager/api/v1/chats?updated_at[from]=${TIMESTAMP}&sort_column=updated_at&sort_direction=asc" | jq
    

The Chats API returns a response similar to the following:
    
    [
      {
        "id": 100,
        ...
        "updated_at": "2025-01-01T00:00:00Z"
      },
      {
        "id": 98,
        ...
        "updated_at": "2025-01-02T00:00:00Z"
      },
      {
        "id": 150,
        ...
        "updated_at": "2025-01-03T00:00:00Z"
      }
    ]
    

Response objects updated on or after the timestamp specified are returned, sorted by date, in ascending order. Use the `updated_at` timestamp from the last object in this response for the timestamp in your next call to the endpoint.

  2. Call the API endpoint again 60 minutes later. The updated chat records since your last request are returned.

  3. Repeat the previous step to continue tailing the endpoint.




### Tail the Agent Activity API endpoint

Unlike the Chat and Call records, the Agent Activity Logs don't get updated and as such don't have an `updated_at` timestamp. You can use the `started_at` timestamp to specify the activity records that you want to retrieve when calling the Agent Activity API endpoint.

To tail the Agent Activity API endpoint every 60 minutes, follow these steps:

  1. Make a request to the Agent Activity API endpoint (`/manager/api/v1/agent_activity_logs`), specifying the following query parameters:

     * `started_at[from]`. Specify that you want activity logs that were started on or after this time.

     * `sort_column`. Specify the field to sort the records by.

     * `sort_direction`. Specify the sort direction of the records in the response.

The following is an example Bash script that uses the `curl` command:
    
    # 1. Define your environment variables (usually set in your shell or .env file)
    export API_HOSTNAME="ccaip-host.uc1.ccaiplatform.com/"
    export API_USER="ccaip-host"
    export API_PASS="CCAI Platform API Key"
    
    # 2. Calculate the timestamp for 60 minutes ago in ISO 8601 format (UTC)
    # For macOS (BSD date):
    # TIMESTAMP=$(date -v-60M -u +"%Y-%m-%dT%H:%M:%SZ")
    # For Linux (GNU date):
    TIMESTAMP=$(date --date='60 minutes ago' -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # 3. Execute the curl command
    # -u handles the Base64 encoding for Basic Auth automatically
    curl -g -u "${API_USER}:${API_PASS}" \
    "https://${API_HOSTNAME}/manager/api/v1/agent_activity_logs?started_at[from]=${TIMESTAMP}&sort_column=started_at&sort_direction=asc" | jq
    

The Agent Activity API returns a response similar to the following:
    
    [
      {
        "id": 100,
        ...
        "started_at": "2025-01-01T00:00:00Z"
      },
      {
        "id": 98,
        ...
        "started_at": "2025-01-02T00:00:00Z"
      },
      {
        "id": 150,
        ...
        "started_at": "2025-01-03T00:00:00Z"
      }
    ]
    

Response objects started on or after the timestamp specified are returned, sorted by date, in ascending order. Use the `started_at` timestamp from the last object in this response for the timestamp in your next call to the endpoint.

  2. Call the Agent Activity API endpoint again 60 minutes later. The updated Agent Activity Log records since your last request are returned.

  3. Repeat the previous step to continue tailing the endpoint.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
