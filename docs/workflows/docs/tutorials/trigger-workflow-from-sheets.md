---
url: https://docs.cloud.google.com/workflows/docs/tutorials/trigger-workflow-from-sheets/
title: Trigger a workflow from Google Sheets \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:26.732261+00:00
---

# Trigger a workflow from Google Sheets  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/tutorials/trigger-workflow-from-sheets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Trigger a workflow from Google Sheets Stay organized with collections  Save and categorize content based on your preferences. 

Connecting [Google Sheets](https://developers.google.com/sheets) to Workflows lets you automate cloud operations directly from spreadsheet data changes. In this tutorial, you configure an Apps Script trigger to call the Workflows API and run an execution when a sheet is edited.

## Objectives

In this tutorial, you will:

  1. Use [Google Forms](https://developers.google.com/forms/), a cloud-based questionnaire and survey solution, to create a form that can submit requests to create virtual machine (VM) instances.
  2. Link a Google Sheets spreadsheet to the form to collect and save any responses.
  3. Use [Google Apps Script](https://developers.google.com/apps-script/), a cloud-based JavaScript platform that lets you programmatically create, read, and edit Google Workspace products, to trigger a workflow whenever a request is approved through an update to the spreadsheet.
  4. Deploy a workflow that calls the [Compute Engine API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/Overview) and creates a Compute Engine VM instance based on the specifications collected through the form. Connectors simplify the calling of other Google Cloud APIs. [Learn more about Workflows connectors](https://docs.cloud.google.com/workflows/docs/connectors).
  5. Test the entire process and confirm that a VM instance is created as expected.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

The tutorial also uses [Google Workspace](https://workspace.google.com). Business-grade services that are not included with Google's free consumer apps are billable.

## Before you begin

You can run some of the following commands in the Google Cloud console, or by using the Google Cloud CLI in either your terminal or Cloud Shell.

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Enable the Compute Engine and Workflows APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,workflows.googleapis.com)

  4. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) as you will associate it with the workflow in this tutorial for testing purposes. New projects that have enabled the Compute Engine API have this service account created with the IAM basic Editor role, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Enable the Compute Engine and Workflows APIs.
         
         gcloud services enable \
             compute.googleapis.com \
             workflows.googleapis.com

  4. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) as you will associate it with the workflow in this tutorial for testing purposes. New projects that have enabled the Compute Engine API have this service account created with the IAM basic Editor role, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

You can retrieve your project number:
         
         gcloud projects describe PROJECT_ID

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Create a form to request VM instances

Create a form that can be used to submit a request to create a Compute Engine virtual machine (VM) instance. By default, when you create a form through Google Forms, it's saved in [Google Drive](https://drive.google.com).

  1. Go to [forms.google.com](https://forms.google.com). 
  2. Click **Blank** ![Plus](https://lh3.googleusercontent.com/anBD83lVdJYMSbLhOXIulHzmEGPr0uJRfiomsujvgYDHF0UlSHRhpJWca3hcw68T5A=w36-h36). 

A new form opens.

  3. Create a form with five required sections. The form should appear similar to the following: 

**View sample form**

![Example of form to request creation of Google Cloud Virtual Machine](https://docs.cloud.google.com/static/workflows/images/workspace-form-example.png)**Machine name**|  Short answer text  
---|---  
**Zone**|  Dropdown:
     1. us-central1-a
     2. us-central1-b
     3. us-central1-c
     4. us-central1-f  
**Type**|  Dropdown:
     1. e2-micro
     2. e2-small
     3. e2-medium
     4. e2-standard-2
     5. e2-standard-4  
**Disk size (GB)**|  Short answer text  
**Operating system**|  Dropdown:
     1. debian-10
     2. centos-stream-9
     3. cos-93-lts
     4. cos-97-lts  
  4. Enable email collection to record the email addresses of people who fill in your form: 
     1. Click **Settings**.
     2. Expand the **Responses** section.
     3. Click the **Collect email addresses** toggle.



## Link a spreadsheet to your form

After you have created a form, link a spreadsheet to it so that you can save your form responses in that spreadsheet. The spreadsheet is saved in [Drive](https://drive.google.com).

  1. Open your form in [Forms](https://forms.google.com).
  2. Click **Responses**.
  3. Click **Link to Sheets**.
  4. In the **Select destination for responses** dialog, select **Create a new spreadsheet**.
  5. Click **Create**.

The linked spreadsheet opens.

  6. In column **H** , add an **Approved?** heading.

  7. Place your cursor in the first row of column **H** and select **Insert > Checkbox**.

The spreadsheet should appear similar to the following:

![Example of linked spreadsheet to collect requests](https://docs.cloud.google.com/static/workflows/images/workspace-sheet-example.png)

Each time the sheet is updated with a response, the checkbox will also appear in the row for that response.




## Extend Google Sheets using Apps Script

Apps Script lets you programmatically create, read, and edit Sheets. Most scripts designed for Sheets manipulate arrays to interact with the cells, rows, and columns in a spreadsheet. For an introduction to using Apps Script with Sheets, see the [Custom function quickstart](https://developers.google.com/apps-script/quickstart/custom-functions).

**Note:** If you're logged into multiple Google Accounts at the same time, you might have trouble accessing Apps Script. Multi-login, or being logged into multiple Google Accounts at once, isn't supported for Apps Script. For more information, see [Fix issues with multiple Google Accounts](https://developers.google.com/apps-script/guides/projects#fix_issues_with_multiple_google_accounts).

  1. Create an Apps Script project from Sheets:

     1. Open your Sheets spreadsheet.
     2. Select **Extensions > Apps Script**.
     3. In the script editor, click **Untitled project**.
     4. Give your project a name and click **Rename**.

Your script is now [bound](https://developers.google.com/apps-script/guides/bound) to your spreadsheet, which gives the script abilities to alter the user interface or respond when the spreadsheet is opened.

A script project represents a collection of Apps Script files and resources. Code files in a script project have a `.gs` extension.

  2. You can use Apps Script to write custom functions that you can use in Sheets just like a built-in function. Custom functions are created using standard JavaScript. Create a function:

     1. Open your Apps Script project.
     2. Click **Editor** code.
     3. A script file appears as a project file named `Code.gs`. To edit the file, select it.
     4. Replace any code in the script editor with the following code which reads the data in your spreadsheet and passes it along as input to a workflow execution:
            
            const PROJECT_ID = "your-project-id";
            const REGION = "us-central1";
            const WORKFLOW = "create-vm-from-form";
            
            function handleEdit(e) {
              var range = e.range.getA1Notation();
              var sheet = e.source;
            
              if (range.length > 1 && range[0] === 'H') {
                if (e.value == "TRUE") {
                  Logger.log("Approved checkbox: true");
            
                  var row = range.slice(1)
                  var email = sheet.getRange('B' + row).getCell(1, 1).getValue()
                  var vmName = sheet.getRange('c' + row).getCell(1, 1).getValue()
                  var zone = sheet.getRange('D' + row).getCell(1, 1).getValue()
                  var machineType = sheet.getRange('E' + row).getCell(1, 1).getValue()
                  var diskSize = sheet.getRange('F' + row).getCell(1, 1).getValue()
                  var imageFamily = sheet.getRange('G' + row).getCell(1, 1).getValue()
                  var imageProject = imageFamily.substring(0, imageFamily.indexOf('-')) + "-cloud"
            
                  const executionPayload = {
                    "argument": "{\"diskSize\": \"" + diskSize + "\", \"email\": \"" + email + "\", \"imageFamily\": \"" + imageFamily + "\", \"imageProject\": \"" + imageProject + "\", \"machineType\": \"" + machineType + "\", \"vmName\": \"" + vmName + "\", \"zone\": \"" + zone +  "\"}"
                  };
            
                  approve(executionPayload);
                }
                else {
                  Logger.log("Approved checkbox: false");
                }
              }
            }
            
            function approve(executionPayload) {
              const headers = {
                "Authorization": "Bearer " + ScriptApp.getOAuthToken()
              };
            
              const params = {
                "method": 'post',
                "contentType": 'application/json',
                "headers": headers,
                "payload": JSON.stringify(executionPayload)
              };
            
              const url = "https://workflowexecutions.googleapis.com/v1/projects/" + PROJECT_ID + "/locations/" + REGION + "/workflows/" + WORKFLOW + "/executions";
            
              Logger.log("Workflow execution request to " + url);
              var response = UrlFetchApp.fetch(url, params);
              Logger.log(response);
            }

     5. Replace `your-project-id` with your Google Cloud project ID.

You can find your project ID on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.

     6. Click Save save.

  3. Apps Script [installable triggers](https://developers.google.com/apps-script/guides/triggers/installable) let a script project execute a specified function when certain conditions are met, such as when a spreadsheet is opened or edited. Create a trigger:

     1. Open your Apps Script project.
     2. Click **Triggers** alarm.
     3. Click **Add Trigger**.
     4. In the **Add Trigger for YOUR_PROJECT_NAME** dialog, configure the trigger: 
        1. In the **Choose which function to run** list, select **handleEdit**.
        2. In the **Choose which deployment should run** list, select **Head**.
        3. In the **Select event source** list, select **From spreadsheet**.
        4. In the **Select event type** list, select **On edit**.
        5. In the **Failure notification settings** list, select **Notify me daily**.
     5. Click **Save**.
     6. If you receive a prompt to choose a Google Account, select the appropriate account, and then click **Allow**.

This allows your Apps Script project to see, edit, create, and delete your Sheets spreadsheets; and to connect to an external service.

  4. An Apps Script project [manifest file](https://developers.google.com/apps-script/concepts/manifests) is a JSON file that specifies basic project information that Apps Script needs to run a script successfully. Note that the Apps Script editor hides manifest files by default to protect your Apps Script project settings. Edit the manifest file:

     1. Open your Apps Script project.
     2. Click **Project Settings** settings.
     3. Select the **Show "appsscript.json" manifest file in editor** checkbox.
     4. Click **Editor** code.
     5. The manifest file appears as a project file named `appsscript.json`. To edit the file, select it.
     6. The `oauthScopes` field specifies an array of strings. To set the [authorization scopes](https://developers.google.com/apps-script/concepts/scopes) your project uses, add an array with the scopes you want supported. For example: 
            
            {
              "timeZone": "America/Toronto",
              "dependencies": {
              },
              "exceptionLogging": "STACKDRIVER",
              "runtimeVersion": "V8",
              "oauthScopes": [
                "https://www.googleapis.com/auth/script.external_request",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/spreadsheets"
              ]
            }

This sets explicit scopes to:

        * Connect to an external service
        * See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account
        * See, edit, create, and delete all your Sheets spreadsheets
     7. Click Save save.

**Note:** To protect your project settings, hide the manifest when you are done editing by clearing the **Show "appsscript.json" manifest file in editor** checkbox.



## Deploy a workflow that creates a VM instance

Deploy a workflow that is triggered when a request to create a VM instance is approved. The workflow calls the [Compute Engine API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/Overview) to create a Compute Engine VM instance based on the specifications collected through the form.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the new workflow: `create-vm-from-form`.

  4. In the **Region** list, select **us-central1 (Iowa)**.

  5. For the **Service account** , select the Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`).

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:
         
         main:
            params: [input]
            steps:
            - init:
                assign:
                     - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                     - zone: ${input.zone}
                     - machineType: ${input.machineType}
                     - diskSize: ${input.diskSize}
                     - imageProject: ${input.imageProject}
                     - imageFamily: ${input.imageFamily}
                     - vmName: ${input.vmName}
                     - email: ${input.email}
            - createResource:
                call: googleapis.compute.v1.instances.insert
                args:
                    project: ${projectId}
                    zone: ${zone}
                    body:
                        name: ${vmName}
                        machineType: ${"projects/" + projectId + "/zones/" + zone + "/machineTypes/" + machineType}
                        disks:
                         - initializeParams:
                             diskSizeGb: ${diskSize}
                             sourceImage: ${"projects/" + imageProject + "/global/images/family/" + imageFamily}
                           type: PERSISTENT
                           boot: true
                           autoDelete: true
                        networkInterfaces:
                         - network: "global/networks/default"
                result: insertResult
            - retStep:
                return: ${insertResult}

  8. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch create-vm-from-form.yaml

  2. In a text editor, copy the following workflow to your source code file:
         
         main:
            params: [input]
            steps:
            - init:
                assign:
                     - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                     - zone: ${input.zone}
                     - machineType: ${input.machineType}
                     - diskSize: ${input.diskSize}
                     - imageProject: ${input.imageProject}
                     - imageFamily: ${input.imageFamily}
                     - vmName: ${input.vmName}
                     - email: ${input.email}
            - createResource:
                call: googleapis.compute.v1.instances.insert
                args:
                    project: ${projectId}
                    zone: ${zone}
                    body:
                        name: ${vmName}
                        machineType: ${"projects/" + projectId + "/zones/" + zone + "/machineTypes/" + machineType}
                        disks:
                         - initializeParams:
                             diskSizeGb: ${diskSize}
                             sourceImage: ${"projects/" + imageProject + "/global/images/family/" + imageFamily}
                           type: PERSISTENT
                           boot: true
                           autoDelete: true
                        networkInterfaces:
                         - network: "global/networks/default"
                result: insertResult
            - retStep:
                return: ${insertResult}

  3. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy create-vm-from-form \
             --source=create-vm-from-form.yaml \
             --location=us-central1 \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can retrieve your project number:
         
         gcloud projects describe PROJECT_ID




## Test the end-to-end flow

To confirm that all is working as expected, try running through the entire process.

  1. Send your form to yourself and answer the questions appropriately.

Ensure that the specifications you use to create a VM instance are valid; otherwise, your workflow execution will fail. For more information, see [Compute Engine general-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines).

  2. To submit your response, click **Submit**.

  3. Open your form in [Forms](https://forms.google.com).

  4. Click **Responses**.

  5. Click **View in Sheets**.

Your linked spreadsheet opens.

  6. In the row for your response, select the **Approved?** checkbox.

  7. Open your Apps Script project.

  8. Click **Executions** playlist_play.

Your trigger should be executed and listed with a status of `Completed`.

  9. Confirm that the `create-vm-from-form` workflow completed successfully:

###  Console 

     1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

     2. On the **Workflows** page, click the **create-vm-from-form** workflow to go to its details page.

     3. On the **Workflow details** page, to retrieve the details for a particular execution, click the appropriate execution ID.

The **Execution state** should be **Succeeded** and, in the Input pane, you should see the VM specifications that you requested.

###  gcloud 

Retrieve a list of your workflow's execution attempts:
    
    gcloud workflows executions list create-vm-from-form

The result should be similar to the following:
    
    NAME: projects/918619793306/locations/us-central1/workflows/create-vm-from-form/executions/d8947ecb-9ccb-4ea1-ba10-e5c10414e3be
    STATE: SUCCEEDED
    START_TIME: 2023-01-24T15:07:40.404741791Z
    END_TIME: 2023-01-24T15:07:55.649373625Z

  10. Confirm that a new VM was created as expected:

###  Console 

In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

Your VM instance should be listed with a status indicating that it is running.

###  gcloud 

Retrieve an aggregate list of all VMs in all zones for a project:
         
         gcloud compute instances list

Your VM instance should be listed with a status indicating that it is running.

For more information about the `gcloud compute instances list` command, see its [reference page](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list).




## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and wish to keep it without the changes added in this tutorial, delete resources created for the tutorial.

### Delete the project

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



### Delete resources created in this tutorial

  1. [Delete files in Drive](https://support.google.com/docs/answer/2375102).
  2. [Delete a Compute Engine VM instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).
  3. [Delete a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#delete-workflow).



## What's next

  * [Write to Sheets from a workflow](https://docs.cloud.google.com/workflows/docs/write-to-google-sheets).
  * [Pause and resume a workflow using callbacks and Sheets](https://docs.cloud.google.com/workflows/docs/tutorials/workflow-waits-callback-sheets).
  * [Learn more about the Forms connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/forms/Overview).
  * [Explore the Google Workspace Learning Center](https://support.google.com/a/users#topic=11499463).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
