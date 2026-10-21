---
url: https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-langchain-service/
title: Quickstart: Build and deploy a Python (LangChain) web app to Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:07.754540+00:00
---

# Quickstart: Build and deploy a Python (LangChain) web app to Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-langchain-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Build and deploy a Python (LangChain) web app to Cloud Run

Cloud Run lets you build and deploy LangChain applications that use Gemini to respond to queries. In this quickstart, you deploy a Python web app that answers questions about city capitals, with Cloud Run automatically building the container when you [deploy from source code](https://docs.cloud.google.com/run/docs/deploying-source-code).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).

  15. Enable the Cloud Run Admin API and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable run.googleapis.com cloudbuild.googleapis.com

After the Cloud Run Admin API is enabled, the Compute Engine default service account is automatically created.

  16. Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator).
  17. You require an API key from Google AI Studio to deploy the LangChain app with a Gemini model. To generate an API key using Google AI studio, see [Using Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key) in the Gemini API documentation. You will reference this key when deploying your service.



### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the project
  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant the Cloud Build service account access to your project

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior.

For Cloud Build to build your sources, grant the Cloud Build service account the [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) role on your project:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCOUNT_EMAIL_ADDRESS \
        --role=roles/run.builder

Replace `PROJECT_ID` with your Google Cloud project ID and `SERVICE_ACCOUNT_EMAIL_ADDRESS` with the email address of the Cloud Build service account. If you're using the Compute Engine default service account as the Cloud Build service account, then use the following format for the service account email address:
    
    
    PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number.

For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Write the sample application

To write an application in Python:

  1. Create a new directory named `langchain-gemini-fastapi-app` and change directory into it:
         
         mkdir langchain-gemini-fastapi-app
         cd langchain-gemini-fastapi-app
         

  2. Create a file named `main.py` and paste the following code into it:
         
         import os
         import uvicorn
         from fastapi import FastAPI, HTTPException
         from pydantic import BaseModel
         from langchain_google_genai import ChatGoogleGenerativeAI
         from langchain_core.prompts import ChatPromptTemplate
         from langchain_core.output_parsers import StrOutputParser
         
         # Initialize FastAPI
         app = FastAPI(title="LangChain Gemini Cloud Run App")
         
         # 1. Setup Gemini Model
         # We expect GOOGLE_API_KEY to be set in the environment variables
         llm = ChatGoogleGenerativeAI(
           model="gemini-2.5-flash",
           temperature=0.7
         )
         
         # 2. Define the Chain
         prompt = ChatPromptTemplate.from_template("You are a helpful assistant. Answer the following question concisely: {topic}")
         output_parser = StrOutputParser()
         
         # Chain: Prompt -> Model -> String Parser
         chain = prompt | llm | output_parser
         
         # 3. Define Request Model
         class QueryRequest(BaseModel):
           topic: str
         
         # 4. Define Endpoint
         @app.post("/chat")
         async def chat(request: QueryRequest):
           try:
               response = await chain.ainvoke({"topic": request.topic})
               return {"response": response}
           except Exception as e:
               raise HTTPException(status_code=500, detail=str(e))
         
         @app.get("/")
         def health_check():
           return {"status": "ok", "service": "Gemini-FastAPI"}
         

  3. Create a file named `requirements.txt` and paste the following code into it:
         
         fastapi
         uvicorn
         langchain
         langchain-google-genai
         python-dotenv
         




## Deploy to Cloud Run from source

Deploy from source automatically builds a container image from source code and deploys it.

To deploy from source using the following command:
    
    
      gcloud run deploy gemini-fastapi-service \
        --source . \
        --region us-central1 \
        --no-allow-unauthenticated \
        --set-env-vars GEMINI_API_KEY=API_KEY
    

Replace API_KEY with your [Google AI Studio API key](https://ai.google.dev/gemini-api/docs/api-key). For production, it is recommended to use [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) to handle the API key, rather than plain environment variables.

Cloud Run displays the service URL, such as `https://gemini-fastapi-service-xyz-uc.a.run.app`, after you successfully deploy the app.

**Success:** You deployed a LangChain web app to Cloud Run.

## Test your Cloud Run service

Test your service by sending a query to the agent using the following curl command:
    
    
      curl -X POST YOUR-SERVICE-URL/chat \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
        -d '{"topic": "What is the capital of France?"}'
    

Replace YOUR-SERVICE-URL with your service's URL.

The agent sends the following response:
    
    
      {
      "response": "Paris"
      }
    

To verify your service is working correctly, [check the **Logs** tab of the Cloud Run service](https://docs.cloud.google.com/run/docs/logging#service-logs).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this quickstart.

### Delete your repository

Cloud Run doesn't charge you when your deployed service isn't in use. However, you might still be [charged for storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing). To delete Artifact Registry repositories, follow the steps in [Delete repositories](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#delete) in the Artifact Registry documentation.

### Delete your service

Cloud Run services don't incur costs until they receive requests. To delete your Cloud Run service, follow one of these steps:

### Console

To delete a service:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the service you want to delete in the services list, and click its checkbox to select it.

  3. Click **Delete**. This deletes all revisions of the service.




###  gcloud 

To delete a service, run the following command:
    
    
    gcloud run services delete SERVICE --region REGION

Replace the following:

  * SERVICE: name of your service.
  * REGION: Google Cloud region of the service.



### Delete your test project

Deleting your Google Cloud project stops billing for all resources in that project. To release all Google Cloud resources in your project, follow these steps:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

For more information on building a container from code source and pushing to a repository, see:

  * [Developing Cloud Run services](https://docs.cloud.google.com/run/docs/developing)
  * [Building Containers](https://docs.cloud.google.com/run/docs/building/containers)
  * [Test a Cloud Run service locally](https://docs.cloud.google.com/run/docs/testing/local)
  * [Deploying from source code](https://docs.cloud.google.com/run/docs/deploying-source-code)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
