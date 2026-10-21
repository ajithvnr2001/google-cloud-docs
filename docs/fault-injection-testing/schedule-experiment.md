---
url: https://docs.cloud.google.com/fault-injection-testing/schedule-experiment/
title: Schedule an experiment \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:02:13.674254+00:00
---

# Schedule an experiment  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/schedule-experiment/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Schedule an experiment Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to schedule experiments in Fault Injection Testing and how to use external scheduling services to automate your resilience testing.

By scheduling experiments, you can automate your testing processes and run experiments during periods that minimize impact on your users, such as:

  * Off-peak hours or planned maintenance windows.
  * Regularly scheduled game days or chaos engineering drills.
  * Automated testing pipelines (CI/CD) to verify resilience before deployment.



Scheduling experiments helps you establish continuous validation of your systems' fault tolerance without requiring manual intervention for every run.

## How scheduled experiments work

Fault Injection Testing does not include a built-in scheduling service. Instead, you schedule experiments by integrating Fault Injection Testing with an external scheduling service, such as Cloud Scheduler.

To schedule an experiment, you configure the external scheduler to call the Fault Injection Testing API or run a `gcloud` command at a specific time. To support this integration, Fault Injection Testing provides the `startOnCreateEnabled` parameter. When set to `true`, this parameter tells the system to automatically start the experiment immediately after it is created.

### Selecting targets for scheduled experiments

The target resources for a scheduled experiment are defined within the experiment template, not within the scheduling configuration itself. Here's how Fault Injection Testing handles targets:

  * When you create an experiment template, you define the type of fault and the selection criteria for your target resources. Examples of resources include specific VM instances, resources with matching tags, or resources in a specific zone.
  * When you configure your external scheduler, the API payload references your experiment template.
  * At the scheduled time, the external scheduler triggers the creation of the experiment. Fault Injection Testing then evaluates the target selection rules in the template at that moment to determine which resources are affected.



If your template targets VMs based on a tag, the scheduled experiment affects whatever VMs have that tag at the exact time the experiment runs.

## Set up a scheduled experiment

Before proceeding, ensure you have the `roles/faulttesting.operator` or `roles/faulttesting.admin` role.

### Configure a schedule using the Google Cloud console and Cloud Scheduler

Although you cannot create schedules directly inside the Fault Injection Testing console, the console provides the parameters you need to set up a job in Cloud Scheduler.

  1. In the Google Cloud console, navigate to the **Experiment templates** page.
  2. Select a template to view its details.
  3. In the details page, take note of the following:

     * The JSON payload, which includes `"startOnCreateEnabled": true`.
     * The REST API endpoint URL for creating an experiment.

You'll use them in Cloud Scheduler.

  4. In the Google Cloud console, navigate to the [**Cloud Scheduler**](https://console.cloud.google.com/cloudscheduler) page and click **Create job**.

  5. Define your job's schedule and timezone.

  6. Under **Target type** , select **HTTP**.

  7. Set the **URL** to the REST API endpoint URL from the **Experiment templates** details page.

  8. Set the **HTTP method** to **POST**.

  9. In the **Body** field, enter the JSON payload:
         
         {
           "experimentTemplate": "projects/PROJECT_ID/locations/REGION/experimentTemplates/TEMPLATE_ID",
           "startOnCreateEnabled": true,
           "description": "DESCRIPTION"
         }
         

  10. Configure authentication for the job. See best practices for service account recommendations.

  11. Click **Create**.




### Configure a schedule using the Google Cloud CLI

If you are using scripts or tools that run shell commands, you can schedule experiments by configuring Cloud Scheduler or your own scheduler to run the `gcloud alpha fault-testing experiments create` command with the `--start-on-create-enabled` flag.

Run the following command to create and immediately start an experiment instance:
    
    
    gcloud alpha fault-testing experiments create EXPERIMENT_ID \
        --experiment-template=TEMPLATE_ID \
        --location=REGION \
        --start-on-create-enabled \
        [--description="DESCRIPTION"] \
        [--project=PROJECT_ID]
    

  * `EXPERIMENT_ID`: A unique identifier for the experiment run. Since this command is automated, your script should generate a unique ID for each run. For example, you can append a timestamp: `scheduled-exp-$(date +%s)`.
  * `TEMPLATE_ID`: The ID of your pre-configured experiment template.
  * `REGION`: The Google Cloud region where the experiment runs.
  * `--start-on-create-enabled`: This flag tells Fault Injection Testing to start the experiment immediately after creation.
  * `DESCRIPTION`: (Optional) A description of the experiment run.
  * `PROJECT_ID`: (Optional) Your Google Cloud project ID.



#### Manage experiment runs

Each scheduled execution creates a new, distinct experiment instance. You can manage these instances using the following commands:

  * To list all experiment runs:
        
        gcloud alpha fault-testing experiments list --location=REGION
        

  * To view details of a specific run:
        
        gcloud alpha fault-testing experiments describe EXPERIMENT_ID --location=REGION
        

  * To stop a running experiment early:
        
        gcloud alpha fault-testing experiments stop EXPERIMENT_ID --location=REGION
        




## Best practices

When scheduling experiments, consider the following best practices:

  * **Use a dedicated service account.** When configuring your scheduler (such as Cloud Scheduler), associate it with a dedicated service account. Grant this service account only the minimum permissions required to manage experiments, such as `roles/faulttesting.operator` or `roles/faulttesting.admin` on your project.
  * **Generate unique experiment IDs.** When triggering experiments using scripts, ensure your script generates a unique experiment ID for each run to avoid resource name collisions.
  * **Use descriptive names or descriptions.** Every scheduled run creates a _new_ experiment instance. It does not restart or overwrite previous experiments. Use descriptive names or descriptions to help trace runs back to their schedule.
  * **Monitor schedule failures.** External triggers can fail due to network issues, credential expiration, or API quotas. Set up monitoring and alerts on your scheduler jobs to notify you if a job fails to run or receives an error response.
  * **Coordinate with exclusion windows.** Verify that your scheduled experiments don't overlap with active [exclusion windows](https://docs.cloud.google.com/fault-injection-testing/exclusion-windows). If a scheduled experiment is triggered during an exclusion window, Fault Injection Testing blocks the run, and the experiment fails to start.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
