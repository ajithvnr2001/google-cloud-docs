---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/secret-manager/
title: Configure secrets with Secret Manager \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:44:59.171186+00:00
---

# Configure secrets with Secret Manager  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Configure secrets with Secret Manager Stay organized with collections  Save and categorize content based on your preferences. 

You can use Secret Manager's Python client with Agent Platform Pipelines to access secrets stored on Secret Manager.

## Create a secret using Google Cloud console

  1. [Enable the Secret Manager API](https://console.cloud.google.com/apis/library/secretmanager.googleapis.com) in Google Cloud console.

  2. Go to the **Secret Manager** page in the Cloud console.

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  3. On the Secret Manager page, click **Create Secret**.

  4. On the **Create secret** page, under Name, enter a name for the secret (for example `universe-secret).

  5. To add a secret version when creating the initial secret, in the **Secret value** field, enter a value for the secret (for example `42`).

  6. Choose your region.

  7. Click the **Create secret** button.




## Build and run a pipeline with Python function based components

The following is a sample component that prints out the previously created secret.

  1. Grant the service account that runs the pipeline with the Secret Manager permission. See the "Configure a service account with granular permissions" section of [Configure your Google Cloud project for Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-project#service-account) for more information.

  2. Using Kubeflow Pipelines SDK, build a simple pipeline with one task.
         
         from kfp import compiler
          from kfp import dsl
         
          # A simple component that prints a secret stored in Secret Manager
          # Be sure to specify "google-cloud-secret-manager" as one of packages_to_install
          @dsl.component(
              packages_to_install=['google-cloud-secret-manager']
          )
          def print_secret_op(project_id: str, secret_id: str, version_id: str) -> str:
              from google.cloud import secretmanager
         
              secret_client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
              secret_name = f'projects/{project_id}/secrets/{secret_id}/versions/{version_id}'
              response = secret_client.[access_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_access_secret_version)(request={"name": secret_name})
              payload = response.payload.data.decode("UTF-8")
              answer = "The secret is: {}".format(payload)
              print(answer)
              return answer
         
          # A simple pipeline that contains a single print_secret task
          @dsl.pipeline(
              name='secret-manager-demo-pipeline')
          def secret_manager_demo_pipeline(project_id: str, secret_id: str, version_id: str):
              print_secret_task = print_secret_op(project_id, secret_id, version_id)
         
          # Compile the pipeline
          compiler.Compiler().compile(pipeline_func=secret_manager_demo_pipeline,
                                      package_path='secret_manager_demo_pipeline.yaml')
         

  3. Run the pipeline using the Vertex AI SDK.
         
         from google.cloud import aiplatform
         
          parameter_values = {
              "project_id": PROJECT_ID,
              "secret_id": SECRET_ID,
              "version_id": VERSION_ID
          }
         
          aiplatform.[init](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.html)(
              project=PROJECT_ID,
              location=REGION,
          )
         
          job = aiplatform.[PipelineJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.PipelineJob.html)(
              display_name=f'test-secret-manager-pipeline',
              template_path='secret_manager_demo_pipeline.yaml',
              pipeline_root=PIPELINE_ROOT,
              enable_caching=False,
              parameter_values=parameter_values
          )
         
          job.submit(
              service_account=SERVICE_ACCOUNT
          )
         

Replace the following:

     * PROJECT_ID: The Google Cloud project that this pipeline runs in.
     * SECRET_ID: The secret ID created in previous steps (for example `universe-secret`).
     * VERSION_ID: The version name of the secret.
     * REGION: The region that this pipeline runs in.
     * PIPELINE_ROOT: Specify a Cloud Storage URI that your pipelines service account can access. The artifacts of your pipeline runs are stored within the pipeline root.
     * SERVICE_ACCOUNT: The email address of the service account you created with Secret Manager Accessor permission.



In the output of the `job.submit()` function, you should be able to click the link that brings you to view the pipeline execution in the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
