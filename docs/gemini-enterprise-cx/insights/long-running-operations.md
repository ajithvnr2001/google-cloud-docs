---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations/
title: Get long-running operations \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:33.717534+00:00
---

# Get long-running operations  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Get long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

Some methods return a long-running operation. Long-running methods are asynchronous, and the operation might not be completed when the method returns a response. You can poll the operation to check on its status.

## Get an operation status

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.operations.get`



The following shows how to poll an operation's status by calling the `get` method on the [`Operation`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.operations) resource.

### REST

Refer to the [`operations:get`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.operations/get) API endpoint for complete details. When the operation has completed, a `state` value of `SUCCESSFUL` is returned. The following example demonstrates the expected JSON output when a `CreateIssueModel` operation has completed. Your output might vary depending on which API produced the operation.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * OPERATION_ID: the ID of the conversation you want to analyze. This value was returned when you created the analysis.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.contactcenterinsights.v1.CreateIssueModelMetadata",
        "createTime": "2021-01-20T10:10:10.123000Z",
        "endTime": "2021-01-20T11:11:11.456000Z",
        "request": {
          "parent": "projects/PROJECT_ID/locations/us-central1",
          "issueModel": {
            "displayName": "MODEL_NAME",
            "inputDataConfig": {
              "medium": "CHAT",
              "trainingConversationsCount": "12000",
              "filter": "medium=\"CHAT\""
            }
          }
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.contactcenterinsights.v1.IssueModel",
        "name": "projects/PROJECT_ID/locations/us-central1/issueModels/ISSUE_MODEL_ID",
        "displayName": "my-model",
        "createTime": "2021-01-20T11:11:11.456000Z",
        "state": "UNDEPLOYED",
        "inputDataConfig": {
          "medium": "CHAT",
          "trainingConversationsCount": "12000",
          "filter": "medium=\"CHAT\""
        },
        "trainingStats": {
          "analyzedConversationsCount": "8000",
          "issueStats": {
            "projects/PROJECT_ID/locations/us-central1/issueModels/ISSUE_MODEL_ID/issues/123000": {
              "issue": "projects/$PROJECT/locations/us-central1/issueModels/ISSUE_MODEL_ID/issues/123000",
              "labeledConversationsCount": "10"
            },
            "projects/PROJECT_ID/locations/us-central1/issueModels/ISSUE_MODEL_ID/issues/456000": {
              "issue": "projects/$PROJECT/locations/us-central1/issueModels/ISSUE_MODEL_IDL/issues/456000",
              "labeledConversationsCount": "20"
            },
            ...
          }
        }
      }
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contact_center_insights_v1
    from google.longrunning import operations_pb2
    
    
    def get_operation(operation_name: str) -> operations_pb2.Operation:
        """Gets an operation.
    
        Args:
            operation_name:
                The operation name.
                Format is 'projects/{project_id}/locations/{location_id}/operations/{operation_id}'.
                For example, 'projects/my-project/locations/us-central1/operations/123456789'.
    
        Returns:
            An operation.
        """
        # Construct an Insights client that will authenticate via Application Default Credentials.
        # See authentication details at https://cloud.google.com/docs/authentication/production.
        insights_client = contact_center_insights_v1.ContactCenterInsightsClient()
    
        # Call the Insights client to get the operation.
        operation = insights_client.transport.operations_client.get_operation(
            operation_name
        )
        if operation.done:
            print("Operation is done")
        else:
            print("Operation is in progress")
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
    import com.google.longrunning.[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html);
    import java.io.IOException;
    
    public class GetOperation {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace this variable before running the sample.
        String operationName = "projects/my_project_id/locations/us-central1/operations/12345";
    
        getOperation(operationName);
      }
    
      public static [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) getOperation(String operationName) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client = [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create()) {
          [OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html) operationsClient = client.[getOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html#com_google_cloud_contactcenterinsights_v1_ContactCenterInsightsClient_getOperationsClient__)();
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) operation = operationsClient.[getOperation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html#com_google_longrunning_OperationsClient_getOperation_java_lang_String_)(operationName);
    
          System.out.printf("Got operation %s%n", operation.[getName](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getName__)());
          return operation;
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const operationName = 'projects/my_project_id/locations/us-central1/operations/my_operation_id';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function getOperation() {
      const [operation] = await client.[operationsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/v1.contactcenterinsightsclient.html).getOperation({
        name: operationName,
      });
      console.info(`Got operation ${operation.name}.`);
    }
    getOperation();

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
