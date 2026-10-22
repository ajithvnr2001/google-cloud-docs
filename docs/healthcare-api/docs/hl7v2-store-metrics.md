---
url: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-store-metrics/
title: View HL7v2 store metrics \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:40.638588+00:00
---

# View HL7v2 store metrics  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-store-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  View HL7v2 store metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the following HL7v2 store metrics:

  * The number of HL7v2 messages for a given HL7v2 message type, such as `ADT` or `ORU`.
  * The [Structured Storage](https://cloud.google.com/healthcare-api/pricing#data_storage) size, in bytes, of all HL7v2 messages for a given HL7v2 message type.



You can use these metrics to do the following:

  * Estimate future costs based on current usage.
  * Track how an HL7v2 store grows and changes over time.
  * Ensure that the number of HL7v2 messages matches the number that you [imported](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-import-export).



Modifications to HL7v2 data, such as storing, deleting, or editing the data, are asynchronous. There might be a delay between when you modify the data and when the modifications are shown in the HL7v2 store metrics.

The following samples show how to view HL7v2 store metrics.

### Console

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the HL7v2 store whose metrics you want to view.

  3. In the **Data stores** list, select the HL7v2 store whose metrics you want to view. The **Data store details** page is displayed.

  4. Click the **Metrics** tab.

The tab shows the following metrics on a scorecard:

     * **Total number of message types**
     * **Total number of messages**
     * **Total size of messages**

The metrics table contains the following columns:

Column | Description  
---|---  
`Message type` | The message type, such as `ADT`, `ORM`, or `ACK`.  
`Number of messages` | The number of messages of a given message type.  
`Total size` | The total size of all the messages of a given message type.  
  5. To filter the table data, enter the filter criteria in the **Filter** field.

You can filter using the message type, the number of messages, and the total size of a message type. For example, to filter the **Total size** column, you can select the filter criteria, select an operator, and enter the filter value with the units of the size as they appear in the table. Some valid filter criteria to filter according to the total size are as follows: `Total size:> 2 MiB` and `Total size:>= 2 GiB`.




### REST

Use the [`hl7V2Stores.getHL7v2StoreMetrics`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/getHL7v2StoreMetrics) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the HL7v2 store's parent dataset
  * `HL7V2_STORE_ID`: the HL7v2 store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:getHL7v2StoreMetrics"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:getHL7v2StoreMetrics" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/getHL7v2StoreMetrics). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "metrics": [
        {
          "messageType": "MESSAGE_TYPE",
          "count": "COUNT",
          "structuredStorageSizeBytes": "STRUCTURED_STORAGE_BYTES"
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
