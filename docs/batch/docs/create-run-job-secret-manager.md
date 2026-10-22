---
url: https://docs.cloud.google.com/batch/docs/create-run-job-secret-manager/
title: Protect sensitive data using Secret Manager with Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:30.673129+00:00
---

# Protect sensitive data using Secret Manager with Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Protect sensitive data using Secret Manager with Batch Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to protect sensitive data that you want to specify for a Batch job by using Secret Manager secrets.

[Secret Manager secrets](https://docs.cloud.google.com/secret-manager/docs/overview) protect sensitive data through encryption. In a Batch job, you can specify one or more existing secrets to securely pass the sensitive data they contain, which you can use to do following:

  * Securely define [custom environment variables](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-job-environment-variables) that contain sensitive data.

  * Securely specify the login credentials for a [Docker Registry](https://docs.docker.com/engine/reference/commandline/login/) to let a job's runnables access its private container images.




## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) or [identify a secret](https://docs.cloud.google.com/secret-manager/docs/view-secret-details) for the sensitive data that you want to securely specify for a job. 
  3. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  4. To ensure that the job's service account has the necessary permissions to access secrets, ask your administrator to grant the [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) IAM role to the job's service account on the secret. **Important:** You must grant this role to the job's service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 




## Securely pass sensitive data to custom environment variables

To securely pass sensitive data from Secret Manager secrets to custom environment variables, you must define each environment variable in the [secret variables (`secretVariables`) subfield for an environment](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#environment.FIELDS.secretVariables) and specify a secret for each value. Whenever you specify a secret in a job, you must format it as a path to a secret version: `projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION`.

You can create a job that defines secret variables by using the gcloud CLI, Batch API, Java, Node.js, or Python. The following example explains how to create a job that defines and uses a secret variable for the [environment of all runnables (`environment` subfield of `taskSpec`)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.environment).

**Warning:** Batch prints out variables (including any secrets) in plain text. In this example, the job prints the contents of the specified secret in the logs. Scripts like this are strongly discouraged for real world use, because the unencrypted contents of the secret can be recorded in unauthorized places, like Cloud Logging.

### gcloud

  1. Create a JSON file that specifies the job's configuration details and include the `secretVariables` subfield for one or more environments.

For example, to create a basic script job that uses a secret variable in the environment for all runnables, create a JSON file with the following contents:
         
         {
           "taskGroups": [
             {
               "taskSpec": {
                 "runnables": [
                   {
                     "script": {
                       "text": "echo This is the secret: ${SECRET_VARIABLE_NAME}"
                     }
                   }
                 ],
                 "environment": {
                   "secretVariables": {
                     "{SECRET_VARIABLE_NAME}": "projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION"
                   }
                 }
               }
             }
           ],
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

Replace the following:

     * `SECRET_VARIABLE_NAME`: the name of the [secret variable](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Environment.FIELDS.secret_variables). By convention, environment variable names are [capitalized](https://google.github.io/styleguide/shellguide.html#constants-and-environment-variable-names).

To securely access the sensitive data from the variable's Secret Manager secret, specify this variable name in this job's runnables. The secret variable is accessible to all of the runnables that are in the same [environment](https://docs.cloud.google.com/batch/docs/create-run-basic-job#custom-environment-variables) where you define the secret variable.

     * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

     * `SECRET_NAME`: the name of [an existing Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).

     * `VERSION`: the [version](https://docs.cloud.google.com/secret-manager/docs/view-secret-version) of the specified secret that contains the data you want to pass to the job. This can be the version number or `latest`.

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that specifies the `secretVariables` subfield for one or more environments.

For example, to create a basic script job that uses a secret variable in the environment for all runnables, make the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo This is the secret: ${SECRET_VARIABLE_NAME}"
                }
              }
            ],
            "environment": {
              "secretVariables": {
                "{SECRET_VARIABLE_NAME}": "projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION"
              }
            }
          }
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.

  * `SECRET_VARIABLE_NAME`: the name of the [secret variable](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Environment.FIELDS.secret_variables). By convention, environment variable names are [capitalized](https://google.github.io/styleguide/shellguide.html#constants-and-environment-variable-names).

To securely access the sensitive data from the variable's Secret Manager secret, specify this variable name in this job's runnables. The secret variable is accessible to all of the runnables that are in the same [environment](https://docs.cloud.google.com/batch/docs/create-run-basic-job#custom-environment-variables) where you define the secret variable.

  * `SECRET_NAME`: the name of [an existing Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).

  * `VERSION`: the [version](https://docs.cloud.google.com/secret-manager/docs/view-secret-version) of the specified secret that contains the data you want to pass to the job. This can be the version number or `latest`.




###  Java 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateBatchUsingSecretManager {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
        // The name of the secret variable.
        // This variable name is specified in this job's runnables
        // and is accessible to all of the runnables that are in the same environment.
        String secretVariableName = "VARIABLE_NAME";
        // The name of an existing Secret Manager secret.
        String secretName = "SECRET_NAME";
        // The version of the specified secret that contains the data you want to pass to the job.
        // This can be the version number or latest.
        String version = "VERSION";
    
        createBatchUsingSecretManager(projectId, region,
                jobName, secretVariableName, secretName, version);
      }
    
      // Create a basic script job to securely pass sensitive data.
      // The data is obtained from Secret Manager secrets
      // and set as custom environment variables in the job.
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createBatchUsingSecretManager(String projectId, String region,
                                                      String jobName, String secretVariableName,
                                                      String secretName, String version)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                              String.format("echo This is the secret: ${%s}.", secretVariableName))
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          // Construct the resource path to the secret's version.
          String secretValue = String
                  .format("projects/%s/secrets/%s/versions/%s", projectId, secretName, version);
    
          // Set the secret as an environment variable.
          [Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.html).Builder environmentVariable = [Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.html).newBuilder()
              .[putSecretVariables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.Builder.html#com_google_cloud_batch_v1_Environment_Builder_putSecretVariables_java_lang_String_java_lang_String_)(secretVariableName, secretValue);
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
              // Jobs can be divided into tasks. In this case, we have only one task.
              .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
              .setEnvironment(environmentVariable)
              .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
              .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
              .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder()
              .[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task)
              .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html).CLOUD_LOGGING))
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
    
          return result;
        }
      }
    }

###  Node.js 
    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'batch-job-secret-manager';
    // The name of the secret variable.
    // This variable name is specified in this job's runnables
    // and is accessible to all of the runnables that are in the same environment.
    const secretVariableName = 'secretVariableName';
    // The name of an existing Secret Manager secret.
    const secretName = 'secretName';
    // The version of the specified secret that contains the data you want to pass to the job.
    // This can be the version number or latest.
    const version = 'version';
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      script: new batch.Runnable.Script({
        commands: ['-c', `echo This is the secret: ${secretVariableName}`],
      }),
    });
    
    // Construct the resource path to the secret's version.
    const secretValue = `projects/${projectId}/secrets/${secretName}/versions/${version}`;
    
    // Set the secret as an environment variable.
    const environment = new batch.Environment();
    environment.secretVariables[secretVariableName] = secretValue;
    
    const task = new batch.TaskSpec({
      runnables: [runnable],
      environment,
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      labels: {env: 'testing', type: 'script'},
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateUsingSecretManager() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateUsingSecretManager();

###  Python 
    
    
    from typing import Dict, Optional
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_with_secret_manager(
        project_id: str,
        region: str,
        job_name: str,
        secrets: Dict[str, str],
        service_account_email: Optional[str] = None,
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances with passing secrets from secret manager.
        Note: Job's service account should have the permissions to access secrets.
            - Secret Manager Secret Accessor (roles/secretmanager.secretAccessor) IAM role.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
            secrets: secrets, which should be passed to the job. Environment variables should be capitalized
            by convention https://google.github.io/styleguide/shellguide.html#constants-and-environment-variable-names
                The format should look like:
                    - {'SECRET_NAME': 'projects/{project_id}/secrets/{SECRET_NAME}/versions/{version}'}
                version can be set to 'latest'.
            service_account_email (optional): custom service account email
    
        Returns:
            A job object representing the job created.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = (
            "echo Hello world! from task ${BATCH_TASK_INDEX}."
            + f" ${next(iter(secrets.keys()))} is the value of the secret."
        )
        task.runnables = [runnable]
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        envable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Environment](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Environment.html)()
        envable.secret_variables = secrets
        task.environment = envable
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 4
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # Read more about local disks here: https://cloud.google.com/compute/docs/disks/persistent-disks
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        service_account = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ServiceAccount](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ServiceAccount.html)()
        service_account.email = service_account_email
        allocation_policy.service_account = service_account
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "script"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

## Securely access container images requiring Docker registry credentials

To use a container image from a private Docker registry, a runnable must specify login credentials that allow it to access that Docker registry. Specifically, for any container runnable with the [image URI (`imageUri`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Container.FIELDS.image_uri) set to a image from a private Docker registry, you must specify any credentials required to access that Docker registry by using the [username (`username`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Container.FIELDS.username) and [password (`password`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Container.FIELDS.password).

You can protect any sensitive credentials for a Docker registry by specifying existing secrets that contain the information instead of defining these fields directly. Whenever you specify a secret in a job, you must format it as a path to a secret version: `projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION`.

You can create a job that uses container images from a private Docker registry by using the gcloud CLI or Batch API. The following example explains how to create a job that uses a container image from a private Docker registry by specifying the username directly and the password as a secret.

### gcloud

  1. Create a JSON file that specifies the job's configuration details. For any container runnables that use images from a private Docker registry, include any credentials required to access it in the `username` and `password` fields.

For example, to create a basic container job that specifies an image from a private Docker registry, create a JSON file with the following contents:
         
         {
           "taskGroups": [
             {
               "taskSpec": {
                 "runnables": [
                   {
                     "container": {
                       "imageUri": "PRIVATE_IMAGE_URI",
                       "commands": [
                         "-c",
                         "echo This runnable uses a private image."
                       ],
                       "username": "USERNAME",
                       "password": "PASSWORD"
                     }
                   }
                 ],
               }
             }
           ],
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

Replace the following:

     * `PRIVATE_IMAGE_URI`: the image URI for a container image from a private Docker registry. If this image requires any other [container settings](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container), you must include those also.

     * `USERNAME`: the username for the private Docker registry, which can be specified as a secret or directly.

     * `PASSWORD`: the password for the private Docker registry, which can be specified as a secret (recommended) or directly.

For example, to specify the password as a secret, set `PASSWORD` to the following:
           
           projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION
           

Replace the following:

       * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

       * `SECRET_NAME`: the name of [an existing Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).

       * `VERSION`: the [version](https://docs.cloud.google.com/secret-manager/docs/view-secret-version) of the specified secret that contains the data you want to pass to the job. This can be the version number or `latest`.

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create). For any container runnables that use images from a private Docker registry, include any credentials required to access it in the `username` and `password` fields.

For example, to create a basic container job that specifies an image from a private Docker registry, make the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "container": {
                  "imageUri": "PRIVATE_IMAGE_URI",
                    "commands": [
                      "-c",
                      "echo This runnable uses a private image."
                    ],
                    "username": "USERNAME",
                    "password": "PASSWORD"
                }
              }
            ],
          }
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.

  * `PRIVATE_IMAGE_URI`: the image URI for a container image from a private Docker registry. If this image requires any other [container settings](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container), you must include those also.

  * `USERNAME`: the username for the private Docker registry, which can be specified as a secret or directly.

  * `PASSWORD`: the password for the private Docker registry, which can be specified as a secret (recommended) or directly.

For example, to specify the password as a secret, set `PASSWORD` to the following:
        
        projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION
        

Replace the following:

    * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

    * `SECRET_NAME`: the name of [an existing Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).

    * `VERSION`: the [version](https://docs.cloud.google.com/secret-manager/docs/view-secret-version) of the specified secret that contains the data you want to pass to the job. This can be the version number or `latest`.




## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).

  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).

  * Learn more about [environment variables](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-job-environment-variables).

  * Learn more about [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
