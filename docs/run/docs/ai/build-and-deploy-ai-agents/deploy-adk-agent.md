---
url: https://docs.cloud.google.com/run/docs/ai/build-and-deploy-ai-agents/deploy-adk-agent/
title: Build and deploy an AI agent to Cloud Run using the Agent Development Kit (ADK) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:53.696725+00:00
---

# Build and deploy an AI agent to Cloud Run using the Agent Development Kit (ADK)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/ai/build-and-deploy-ai-agents/deploy-adk-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Build and deploy an AI agent to Cloud Run using the Agent Development Kit (ADK) Stay organized with collections  Save and categorize content based on your preferences. 

The [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) framework simplifies the creation, evaluation, and deployment of AI agents. ADK provides a modular, code-first approach to building agents that can reason, plan, and utilize tools.

This tutorial shows you how to build and deploy an AI agent to Cloud Run using ADK for Python. This agent retrieves the weather report for a city you specify.

For more information about hosting your ADK agent using the Google Cloud CLI, see [Deploy to Cloud Run](https://google.github.io/adk-docs/deploy/cloud-run/) in ADK documentation.

## Objectives

  * Write the sample application to define the weather-agent.
  * Deploy the agent to Cloud Run from source.
  * Run your agent to query weather information. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Run](https://cloud.google.com/run)
  * [ Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

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

  6. Enable the Cloud Run Admin API, Vertex AI API, and Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,aiplatform.googleapis.com,cloudbuild.googleapis.com)

  7. [Set up your Cloud Run development environment](https://docs.cloud.google.com/run/docs/setup) in your Google Cloud project.
  8. Install ADK by following the instructions in the [Agent Development Kit documentation](https://google.github.io/adk-docs/get-started/installation/).
  9. If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).




### Required roles

To get the permissions that you need to deploy an AI agent to Cloud Run, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on the project
  * [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Write the sample application

To write an application in Python:

  1. Create a new parent directory named `parent_folder` and change directory into it:
         
         mkdir parent_folder
         cd parent_folder
         

  2. In the `parent_folder` directory, create a new subdirectory named `multi_tool_agent` and change directory into it:
         
         mkdir multi_tool_agent
         cd multi_tool_agent
         

  3. Create an `__init__.py` file to import the agent:
         
         from . import agent
         

  4. Create an `agent.py` file to define the agent for answering questions about the time and weather in a specified city:
         
         import datetime
         from zoneinfo import ZoneInfo
         from google.adk.agents import Agent
         
         def get_weather(city: str) -> dict:
             """Retrieves the current weather report for a specified city.
         
             Args:
                 city (str): The name of the city for which to retrieve the weather report.
         
             Returns:
                 dict: status and result or error msg.
             """
             if city.lower() == "new york":
                 return {
                     "status": "success",
                     "report": (
                         "The weather in New York is sunny with a temperature of 25 degrees"
                         " Celsius (77 degrees Fahrenheit)."
                     ),
                 }
             else:
                 return {
                     "status": "error",
                     "error_message": f"Weather information for '{city}' is not available.",
                 }
         
         def get_current_time(city: str) -> dict:
             """Returns the current time in a specified city.
         
             Args:
                 city (str): The name of the city for which to retrieve the current time.
         
             Returns:
                 dict: status and result or error msg.
             """
         
             if city.lower() == "new york":
                 tz_identifier = "America/New_York"
             else:
                 return {
                     "status": "error",
                     "error_message": (
                         f"Sorry, I don't have timezone information for {city}."
                     ),
                 }
         
             tz = ZoneInfo(tz_identifier)
             now = datetime.datetime.now(tz)
             report = (
                 f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
             )
             return {"status": "success", "report": report}
         
         root_agent = Agent(
             name="weather_time_agent",
             model="gemini-2.5-flash",
             description=(
                 "Agent to answer questions about the time and weather in a city."
             ),
             instruction=(
                 "You are a helpful agent who can answer user questions about the time and weather in a city."
             ),
             tools=[get_weather, get_current_time],
         )
         

  5. Create a `.env` file and add the following variables:
         
         GOOGLE_GENAI_USE_VERTEXAI=TRUE
         GOOGLE_CLOUD_PROJECT=PROJECT_ID
         GOOGLE_CLOUD_LOCATION=REGION
         

Replace the following:

     * PROJECT_ID: the Google Cloud project ID.
     * REGION: the region you plan to deploy your service in.
  6. Navigate to the parent folder directory `parent_folder`, and create a `requirements.txt` file to add the `google-adk` dependency:
         
         google-adk
         

Your source project includes the following structure:
         
         parent_folder/
         ├── requirements.txt
         └── multi_tool_agent/
             ├── __init__.py
             ├── agent.py
             └── .env
         




Your app is finished and ready to be deployed.

## Deploy to Cloud Run from source

Deploy from source automatically builds a container image from source code and deploys it.

  1. In your source code directory (`parent_folder`), deploy to Cloud Run using the following command:
         
         gcloud run deploy --source .

     1. When you are prompted for the service name, press Enter to accept the default name, for example `weather-agent`.

     2. If you are prompted to enable additional APIs on the project, for example, the Artifact Registry API, respond by pressing `y`. 

     3. When you are prompted for region: select the region of your choice, for example `europe-west1`.

     4. If you are prompted to create a repository in the specified region, respond by pressing `y`.

     5. If you are prompted to _allow public access_ : respond `y`. You might not see this prompt if there is a domain restriction organization policy that prevents it; for more details see the Before you begin section.

Then wait a few moments until the deployment is complete. On success, the command line displays the service URL of deployed agent; it will be in the form of the following, `https://weather-agent-123456789101.us-central1.run.app/list-apps`. 




## Run your agent

To use the ADK agent, you can run the following curl commands:

  1. To get the list of apps, run the following command:
         
         curl -X GET SERVICE_URL/list-apps
         

Replace SERVICE_URL with the URL of your deployed service.

  2. To start a session, run the following command:
         
         curl -X POST SERVICE_URL/apps/multi_tool_agent/users/u_123/sessions/s_123 -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}'
         

  3. To query the agent, run the following command:
         
         curl -X POST SERVICE_URL/run \
         -H "Content-Type: application/json" \
         -d "{\"appName\": \"multi_tool_agent\",\"userId\": \"u_123\",\"sessionId\": \"s_123\",\"newMessage\": { \"role\": \"user\", \"parts\": [{ \"text\": \"What's the weather in New York today?\" }]}}"
         




The agent returns the weather information in the results of your query.

For more information and examples about the supported curl commands, see [Use the API Server](https://google.github.io/adk-docs/runtime/api-server) in ADK documentation.

**Success:** You deployed an AI agent using the Agent Development Kit to Cloud Run.

## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
