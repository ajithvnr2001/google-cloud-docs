---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/continuous-tests/
title: Continuous tests and deployment \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:13.326993+00:00
---

# Continuous tests and deployment  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/continuous-tests/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Continuous tests and deployment Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The _continuous tests_ feature automatically runs a set of test cases configured for an environment to verify the intended behavior of the flow versions in that environment.

To prevent a bad version from becoming live in the environment, you can also use _continuous deployment_ to run the same set of verification tests before deploying a flow version to the environment.

## Manage continuous tests and deployment

To manage continuous tests and deployment:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).

  2. Choose your GCP project.

  3. Select your agent.

  4. Click the **Manage** tab.

  5. Click **CI/CD**.

  6. Select an environment from the **Environment name** dropdown menu.

  7. Click the **Continuous tests** tab. The **Test Cases** tab opens by default.

  8. In the **Select test cases** dropdown, select a predefined test case to add to the continuous testing set.

  9. In the **Settings** tab, the **Continuous test** toggle should be on by default. To add continuous deployment, click the **Continuous deployment** toggle.




To view the results of daily continuous tests for an environment, click the **Continuous tests** tab, then **Results**.

To view whether continuous testing is enabled for an environment, click **Environments** under the **Manage** tab. For each environment, the continuous testing status is under the **Continuous Test** column.

###  API 

See the `runContinuousTest` and `deployFlow` methods for the `Environments` type. Go to the Environment API reference

**Select a protocol and version for the Environment reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Environment resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments) |  [Environment resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.environments)  
RPC |  [Environment interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#environments) |  [Environment interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#environments)  
C++ |  [EnvironmentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1EnvironmentsClient.html) |  Not available   
C# |  [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClient) |  Not available   
Go |  [EnvironmentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_EnvironmentsClient) |  Not available   
Java |  [EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient) |  [EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EnvironmentsClient)  
Node.js |  [EnvironmentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.EnvironmentsClient.html) |  [EnvironmentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.EnvironmentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.environments.EnvironmentsClient) |  [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.environments.EnvironmentsClient)  
Ruby |  Not available  |  Not available   
  
Close

[ Previous arrow_back  Experiments  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments)

[ Next Conversation profiles  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-profiles)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
