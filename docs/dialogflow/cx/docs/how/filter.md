---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/filter/
title: List data with a filter \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:21.381151+00:00
---

# List data with a filter  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/filter/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  List data with a filter Stay organized with collections  Save and categorize content based on your preferences. 

When listing data with the API, some list method requests provide a `filter` field. You can use these filters to only return results you are interested in. This [filtering feature](https://google.aip.dev/160) is common across many Google Cloud APIs.

The following examples show how to filter the response when listing test case results.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.cx.v3.[ListTestCaseResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCaseResultsRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[ListTestCaseResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCaseResultsRequest.html).Builder;
    import com.google.cloud.dialogflow.cx.v3.[TestCaseResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCaseResult.html);
    import com.google.cloud.dialogflow.cx.v3.[TestCasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.html);
    import com.google.cloud.dialogflow.cx.v3.[TestCasesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesSettings.html);
    import java.io.IOException;
    
    public class ListTestCaseResults {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String agentId = "my-agent-id";
        String testId = "my-test-id";
        String location = "my-location";
        listTestCaseResults(projectId, agentId, testId, location);
      }
    
      public static void listTestCaseResults(
          String projectId, String agentId, String testId, String location) throws IOException {
        String parent =
            "projects/"
                + projectId
                + "/locations/"
                + location
                + "/agents/"
                + agentId
                + "/testCases/"
                + testId;
    
        Builder req = [ListTestCaseResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCaseResultsRequest.html).newBuilder();
    
        req.setParent(parent);
        req.setFilter("environment=draft");
    
        [TestCasesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesSettings.html) testCasesSettings =
            [TestCasesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesSettings.html).newBuilder()
                .setEndpoint(location + "-dialogflow.googleapis.com:443")
                .build();
    
        // Note: close() needs to be called on the TestCasesClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([TestCasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.html) client = [TestCasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.html).create(testCasesSettings)) {
          for ([TestCaseResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCaseResult.html) element : client.listTestCaseResults(req.build()).iterateAll()) {
            System.out.println(element);
          }
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const parent = `projects/${projectId}/locations/${location}/agents/${agentId}/testCases/${testId}`;
    
    const {TestCasesClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    
    const client = new [TestCasesClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)({
      apiEndpoint: 'global-dialogflow.googleapis.com',
    });
    const req = {
      parent,
      filter: 'environment=draft',
    };
    
    const res = await client.listTestCaseResults(req);
    
    console.log(res);

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.dialogflowcx_v3.services.test_cases.client import TestCasesClient
    from google.cloud.dialogflowcx_v3.types.test_case import ListTestCaseResultsRequest
    
    
    def list_test_case(project_id, agent_id, test_id, location):
        req = ListTestCaseResultsRequest()
        req.parent = f"projects/{project_id}/locations/{location}/agents/{agent_id}/testCases/{test_id}"
        req.filter = "environment=draft"
        client = TestCasesClient(
            client_options={"api_endpoint": f"{location}-dialogflow.googleapis.com"}
        )
        # Makes a call to list all test case results that match filter
        result = client.list_test_case_results(request=req)
        print(result)
        return result
    
    

[ Previous arrow_back  Update data with a FieldMask  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/field-mask)

[ Next Long-running operations  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/long-running-operation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
