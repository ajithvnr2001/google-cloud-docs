---
url: https://docs.cloud.google.com/workflows/docs/tutorials/callbacks-firestore/
title: Create a human-in-the-loop workflow using callbacks \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:55.077509+00:00
---

# Create a human-in-the-loop workflow using callbacks  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/tutorials/callbacks-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Workflows ](https://docs.cloud.google.com/workflows)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Create a human-in-the-loop workflow using callbacks Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create a translation workflow that waits for your input—the human in the loop—and that connects a Firestore database, two Cloud Run functions, the Cloud Translation API, and a web page that uses the Firebase SDK to update in real time.

With Workflows, you can support a _callback endpoint_ (or webhook) that waits for HTTP requests to arrive at that endpoint, resuming the execution of the workflow at a later point in time. In this case, the workflow waits for your input to reject or validate the translation of some text but it could also wait for an external process. For more information, see [Wait using callbacks](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints).

## Architecture

This tutorial creates a web app that lets you do the following:

  1. On the translation web page, enter the text you want translated from English to French. Click **Translate**.
  2. From the web page, a [Cloud Run function](https://cloud.google.com/functions) is called that launches the execution of the workflow. The text to be translated is passed as a parameter both to the function and to the workflow.
  3. The text is saved in a [Cloud Firestore](https://firebase.google.com/docs/firestore/) database. [Cloud Translation API](https://cloud.google.com/translate) is called. The returned translation is stored in the database. The web app is deployed using [Firebase Hosting](https://firebase.google.com/docs/hosting) and updates in real time to display the translated text.
  4. The `create_callback` step in the workflow creates a callback endpoint URL which is also saved in the Firestore database. The web page now displays both a **Validate** and a **Reject** button.
  5. The workflow is now paused and awaits an explicit HTTP POST request to the callback endpoint URL.
  6. You can decide whether to validate or reject the translation. Clicking a button calls a second Cloud Run function which in turn calls the callback endpoint created by the workflow, passing along the approval status. The workflow resumes its execution and saves an approval status of `true` or `false` in the Firestore database.



This diagram provides an overview of the process:

![Workflow with callback](https://docs.cloud.google.com/static/workflows/images/callbacks-tutorial.svg)

## Objectives

  * Deploy a web app.
  * Create a Firestore database to store translation requests.
  * Deploy Cloud Run functions to run the workflow.
  * Deploy and run a workflow to orchestrate the entire process.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [App Engine](https://docs.cloud.google.com/appengine)
  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Cloud Run functions](https://docs.cloud.google.com/functions)
  * [Firestore](https://docs.cloud.google.com/firestore)
  * [Translation](https://docs.cloud.google.com/translate)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the App Engine, Cloud Build, Cloud Run functions, Firestore, Translation, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable appengine.googleapis.com cloudbuild.googleapis.com cloudfunctions.googleapis.com firestore.googleapis.com translate.googleapis.com workflows.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the App Engine, Cloud Build, Cloud Run functions, Firestore, Translation, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable appengine.googleapis.com cloudbuild.googleapis.com cloudfunctions.googleapis.com firestore.googleapis.com translate.googleapis.com workflows.googleapis.com

  14. Update Google Cloud CLI components: 
         
         gcloud components update

  15. Sign in using your account: 
         
         gcloud auth login

  16. Set the project ID and default location used in this tutorial: 
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         export REGION=REGION
         gcloud config set workflows/location ${REGION}

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID. You can find your project ID on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.
     * `REGION`: the supported Workflows [location](https://docs.cloud.google.com/workflows/docs/locations) of your choice.




## Deploy the first Cloud Run function

This Cloud Run function launches the execution of the workflow. The text to be translated is passed as a parameter both to the function and to the workflow.

  1. Create a directory called `callback-translation` and with subdirectories called `invokeTranslationWorkflow`,`translationCallbackCall`, and `public`:
         
         mkdir -p ~/callback-translation/{invokeTranslationWorkflow,translationCallbackCall,public}

  2. Change to the `invokeTranslationWorkflow` directory:
         
         cd ~/callback-translation/invokeTranslationWorkflow

  3. Create a text file with the filename `index.js` that contains the following Node.js code:
         
         const cors = require('cors')({origin: true});
         const {ExecutionsClient} = require('[@google-cloud/workflows](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)');
         const client = new [ExecutionsClient](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)();
         
         exports.invokeTranslationWorkflow = async (req, res) => {
           cors(req, res, async () => {
             const text = req.body.text;
             console.log(`Translation request for "${text}"`);
         
             const PROJECT_ID = process.env.PROJECT_ID;
             const CLOUD_REGION = process.env.CLOUD_REGION;
             const WORKFLOW_NAME = process.env.WORKFLOW_NAME;
         
             const execResponse = await client.createExecution({
               parent: client.workflowPath(PROJECT_ID, CLOUD_REGION, WORKFLOW_NAME),
               execution: {
                 argument: JSON.stringify({text})
               }
             });
             console.log(`Translation workflow execution request: ${JSON.stringify(execResponse)}`);
         
             const execName = execResponse[0].name;
             console.log(`Created translation workflow execution: ${execName}`);
         
             res.set('Access-Control-Allow-Origin', '*');
             res.status(200).json({executionId: execName});
           });
         };

  4. Create a text file with the filename `package.json` that contains the following `npm` metadata:
         
         {
           "name": "launch-translation-workflow",
           "version": "0.0.1",
           "dependencies": {
             "@google-cloud/workflows": "^1.2.5",
             "cors": "^2.8.5"
           }
         }
         

  5. Deploy the function with an HTTP trigger and allow unauthenticated access:
         
         gcloud functions deploy invokeTranslationWorkflow \
         --region=${REGION} \
         --runtime nodejs14 \
         --entry-point=invokeTranslationWorkflow \
         --set-env-vars PROJECT_ID=${GOOGLE_CLOUD_PROJECT},CLOUD_REGION=${REGION},WORKFLOW_NAME=translation_validation \
         --trigger-http \
         --allow-unauthenticated

The function might take a few minutes to deploy. Alternatively, you can [use the Cloud Run functions interface](https://docs.cloud.google.com/functions/docs/deploying/console) in the Google Cloud console to deploy the function.

  6. Once the function is deployed, you can confirm the `httpsTrigger.url` property:
         
         gcloud functions describe invokeTranslationWorkflow

Note the URL that is returned so that you can use it in a later step.




## Deploy the second Cloud Run function

This Cloud Run function makes an HTTP POST request to the callback endpoint created by the workflow, passing along an approval status that reflects whether the translation is validated or rejected.

**Note:** As you are invoking a callback from a Cloud Run function using the same service account as the workflow and in the same project, an OAuth access token is generated in the function itself. In a production application, it is likely that the frontend would make a direct request to the callback endpoint and authentication would take place then. For more information, see [Use IAM to control access](https://docs.cloud.google.com/workflows/docs/use-iam-for-access).

  1. Change to the `translationCallbackCall` directory:
         
         cd ../translationCallbackCall

  2. Create a text file with the filename `index.js` that contains the following Node.js code:
         
         const cors = require('cors')({origin: true});
         const fetch = require('node-fetch');
         
         function isValidCallbackUrl(urlString) {
           try {
             const parsed = new URL(urlString);
             if (parsed.protocol !== 'https:') {
               return false;
             }
             if (parsed.username || parsed.password) {
               return false;
             }
             const isGoogleWorkflowsHost =
               parsed.hostname === 'workflowexecutions.googleapis.com' ||
               /^[a-z0-9-]+-workflowexecutions\.googleapis\.com$/.test(parsed.hostname);
             if (!isGoogleWorkflowsHost) {
               return false;
             }
             const callbackPathRegex = /^\/v1\/projects\/[a-zA-Z0-9_-]+\/locations\/[a-zA-Z0-9_-]+\/workflows\/[a-zA-Z0-9_-]+\/executions\/[a-zA-Z0-9_-]+\/callbacks\/[a-zA-Z0-9_-]+$/;
             return callbackPathRegex.test(parsed.pathname);
           } catch {
             return false;
           }
         }
         
         exports.isValidCallbackUrl = isValidCallbackUrl;
         exports.translationCallbackCall = async (req, res) => {
           cors(req, res, async () => {
             res.set('Access-Control-Allow-Origin', '*');
         
             const {url, approved} = req.body || {};
             if (!url || !isValidCallbackUrl(url)) {
               res.status(400).json({error: 'Invalid or unauthorized callback URL'});
               return;
             }
         
             console.log("Approved? ", approved);
             console.log("URL = ", url);
             const {GoogleAuth} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
             const auth = new [GoogleAuth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
             const token = await [auth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html).getAccessToken();
         
             try {
               const resp = await fetch(url, {
                   method: 'POST',
                   headers: {
                       'accept': 'application/json',
                       'content-type': 'application/json',
                       'authorization': `Bearer ${token}`
                   },
                   body: JSON.stringify({ approved: Boolean(approved) })
               });
               console.log("Response = ", JSON.stringify(resp));
         
               const result = await resp.json();
               console.log("Outcome = ", JSON.stringify(result));
         
               res.status(200).json({status: 'OK'});
             } catch(e) {
               console.error(e);
         
               res.status(500).json({status: 'error'});
             }
           });
         };

  3. Create a text file with the filename `package.json` that contains the following `npm` metadata:
         
         {
           "name": "approve-translation-workflow",
           "version": "0.0.1",
           "dependencies": {
             "cors": "^2.8.5",
             "node-fetch": "^2.6.1",
             "google-auth-library": "^7.1.1"
           }
         }
         

  4. Deploy the function with an HTTP trigger and allow unauthenticated access:
         
         gcloud functions deploy translationCallbackCall \
         --region=${REGION} \
         --runtime nodejs14 \
         --entry-point=translationCallbackCall \
         --trigger-http \
         --allow-unauthenticated

The function might take a few minutes to deploy. Alternatively, you can [use the Cloud Run functions interface](https://docs.cloud.google.com/functions/docs/deploying/console) in the Google Cloud console to deploy the function.

  5. Once the function is deployed, you can confirm the `httpsTrigger.url` property:
         
         gcloud functions describe translationCallbackCall

Note the URL that is returned so that you can use it in a later step.




## Deploy the workflow

A workflow is made up of a series of steps described using the Workflows syntax, which can be written in either YAML or JSON format. This is the workflow's definition. After creating a workflow, you deploy it to make it available for execution.

  1. Change to the `callback-translation` directory:
         
         cd ..

  2. Create a text file with the filename `translation-validation.yaml` and with the following content:
         
         main:
             params: [translation_request]
             steps:
                 - log_request:
                     call: sys.log
                     args:
                         text: ${translation_request}
                 - vars:
                     assign:
                         - exec_id: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                         - text_to_translate: ${translation_request.text}
                         - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/translations/"}
                 - log_translation_request:
                     call: sys.log
                     args:
                         text: ${text_to_translate}
         
                 - store_translation_request:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                         name: ${database_root + exec_id}
                         updateMask:
                             fieldPaths: ['text']
                         body:
                             fields:
                                 text:
                                     stringValue: ${text_to_translate}
                     result: store_translation_request_result
         
                 - translate:
                     call: googleapis.translate.v2.translations.translate
                     args:
                         query:
                             q: ${text_to_translate}
                             target: "FR"
                             format: "text"
                             source: "EN"
                     result: translation_result
                 - assign_translation:
                     assign:
                         - translation: ${translation_result.data.translations[0].translatedText} 
                 - log_translation_result:
                     call: sys.log
                     args:
                         text: ${translation}
         
                 - store_translated_text:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                         name: ${database_root + exec_id}
                         updateMask:
                             fieldPaths: ['translation']
                         body:
                             fields:
                                 translation:
                                     stringValue: ${translation}
                     result: store_translation_request_result   
         
                 - create_callback:
                     call: events.create_callback_endpoint
                     args:
                         http_callback_method: "POST"
                     result: callback_details
                 - log_callback_details:
                     call: sys.log
                     args:
                         text: ${callback_details}
         
                 - store_callback_details:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                         name: ${database_root + exec_id}
                         updateMask:
                             fieldPaths: ['callback']
                         body:
                             fields:
                                 callback:
                                     stringValue: ${callback_details.url}
                     result: store_callback_details_result
         
                 - await_callback:
                     call: events.await_callback
                     args:
                         callback: ${callback_details}
                         timeout: 3600
                     result: callback_request
                 - assign_approval:
                     assign:
                         - approved: ${callback_request.http_request.body.approved}
         
                 - store_approval:
                     call: googleapis.firestore.v1.projects.databases.documents.patch
                     args:
                         name: ${database_root + exec_id}
                         updateMask:
                             fieldPaths: ['approved']
                         body:
                             fields:
                                 approved:
                                     booleanValue: ${approved}
                     result: store_approval_result
         
                 - return_outcome:
                     return:
                         text: ${text_to_translate}
                         translation: ${translation}
                         approved: ${approved}

  3. After creating the workflow, you can deploy it, but do **not** execute the workflow:
         
         gcloud workflows deploy translation_validation --source=translation-validation.yaml




## Create your web app

Create a web app that calls a Cloud Function which launches the execution of the workflow. The web page updates in real time to display the result of the translation request.

  1. Change to the `public` directory:
         
         cd public

  2. Create a text file with the filename `index.html` that contains the following HTML markup. (In a later step, you will modify the `index.html` file and add the Firebase SDK scripts.)
         
         <!DOCTYPE html>
         <html lang="en">
         
         <head>
             <meta charset="UTF-8">
             <meta name="viewport" content="width=device-width">
         
             <title>Frenglish translation — Feature Workflows callbacks</title>
         
             <link rel="stylesheet"
                 href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.0.0-beta.42/dist/themes/base.css">
             <script type="module"
                 src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.0.0-beta.42/dist/shoelace.js"></script>
             <link rel="stylesheet" href="./style.css">
         </head>
         
         <body>
             <h1>Translate from English to French</h1>
         
             <sl-form class="form-overview">
                 <sl-textarea id="text" placeholder="The quick brown fox jumps over the lazy dog."
                     label="English text to translate"></sl-textarea>
                 <p></p>
                 <sl-button id="translateBtn" type="primary">Translate</sl-button>
                 <p></p>
                 <sl-alert id="translation" type="primary">
                     Le rapide renard brun saute au dessus du chien paresseux.
                 </sl-alert>
                 <p></p>
                 <div id="buttonRow" style="display: none;">
                     <sl-button id="validateBtn" type="success">Validate</sl-button>
                     <sl-button id="rejectBtn" type="danger">Reject</sl-button>
                 </div>
                 <p></p>
                 <sl-alert id="validationAlert" type="success">
                     <sl-icon slot="icon" name="check2-circle"></sl-icon>
                     <strong>The translation has been validated</strong><br>
                     Glad that you liked our translation! We'll save it in our database.
                 </sl-alert>
                 <sl-alert id="rejectionAlert" type="danger">
                     <sl-icon slot="icon" name="exclamation-octagon"></sl-icon>
                     <strong>The translation has been rejected</strong><br>
                     A pity the translation isn't good! We'll do better next time!
                 </sl-alert>
                 <p></p>
                 <sl-button id="newBtn" style="display: none;" type="primary">New translation</sl-button>
             </sl-form>
         
             <script src="https://www.gstatic.com/firebasejs/8.6.3/firebase-app.js"></script>
             <script src="https://www.gstatic.com/firebasejs/8.6.3/firebase-firestore.js"></script>
         
             <script>
                 var firebaseConfig = {
                     apiKey: "XXXX",
                     authDomain: "XXXX",
                     projectId: "XXXX",
                     storageBucket: "XXXX",
                     messagingSenderId: "XXXX",
                     appId: "XXXX",
                     measurementId: "XXXX"
                 };
                 // Initialize Firebase
                 firebase.initializeApp(firebaseConfig);
             </script>
             <script src="./script.js" type="module"></script>
         </body>
         
         </html>
         

  3. Create a text file with the filename `script.js` that contains the following JavaScript code:
         
         document.addEventListener("DOMContentLoaded", async function (event) {
             const textArea = document.getElementById("text");
             textArea.focus();
         
             const newBtn = document.getElementById("newBtn");
             newBtn.addEventListener("sl-focus", event => {
                 event.target.blur();
                 window.location.reload();
             });
         
             const translationAlert = document.getElementById("translation");
             const buttonRow = document.getElementById("buttonRow");
         
             var callbackUrl = "";
         
             const validationAlert = document.getElementById("validationAlert");
             const rejectionAlert = document.getElementById("rejectionAlert");
             const validateBtn = document.getElementById("validateBtn");
             const rejectBtn = document.getElementById("rejectBtn");
         
             const translateBtn = document.getElementById("translateBtn");
             translateBtn.addEventListener("sl-focus", async event => {
                 event.target.disabled = true;
                 event.target.loading = true;
                 textArea.disabled = true;
         
                 console.log("Text to translate = ", textArea.value);
         
                 const fnUrl = UPDATE_ME;
         
                 try {
                     console.log("Calling workflow executor function...");
                     const resp = await fetch(fnUrl, {
                         method: "POST",
                         headers: {
                             "accept": "application/json",
                             "content-type": "application/json"
                         },
                         body: JSON.stringify({ text: textArea.value })
                     });
                     const executionResp = await resp.json();
                     const executionId = executionResp.executionId.slice(-36);
                     console.log("Execution ID = ", executionId);
         
                     const db = firebase.firestore();
                     const translationDoc = db.collection("translations").doc(executionId);
         
                     var translationReceived = false;
                     var callbackReceived =  false;
                     var approvalReceived = false;
                     translationDoc.onSnapshot((doc) => {
                         console.log("Firestore update", doc.data());
                         if (doc.data()) {
                             if ("translation" in doc.data()) {
                                 if (!translationReceived) {
                                     console.log("Translation = ", doc.data().translation);
                                     translationReceived = true;
                                     translationAlert.innerText = doc.data().translation;
                                     translationAlert.open = true;
                                 }
                             }
                             if ("callback" in doc.data()) {
                                 if (!callbackReceived) {
                                     console.log("Callback URL = ", doc.data().callback);
                                     callbackReceived = true;
                                     callbackUrl = doc.data().callback;
                                     buttonRow.style.display = "block";
                                 }
                             }
                             if ("approved" in doc.data()) {
                                 if (!approvalReceived) {
                                     const approved = doc.data().approved;
                                     console.log("Approval received = ", approved);
                                     if (approved) {
                                         validationAlert.open = true;
                                         buttonRow.style.display = "none";
                                         newBtn.style.display = "inline-block";   
                                     } else {
                                         rejectionAlert.open = true;
                                         buttonRow.style.display = "none";
                                         newBtn.style.display = "inline-block";
                                     }
                                     approvalReceived = true;
                                 }
                             }
                         }
                     });
                 } catch (e) {
                     console.log(e);
                 }
                 event.target.loading = false;
             });
         
             validateBtn.addEventListener("sl-focus", async event => {
                 validateBtn.disabled = true;
                 rejectBtn.disabled = true;
                 validateBtn.loading = true;
                 validateBtn.blur();
         
                 // call callback
                 await callCallbackUrl(callbackUrl, true);
             });
         
             rejectBtn.addEventListener("sl-focus", async event => {
                 rejectBtn.disabled = true;
                 validateBtn.disabled = true;
                 rejectBtn.loading = true;
                 rejectBtn.blur();
         
                 // call callback
                 await callCallbackUrl(callbackUrl, false);
             });
         
         });
         
         async function callCallbackUrl(url, approved) {
             console.log("Calling callback URL with status = ", approved);
         
             const fnUrl = UPDATE_ME;
             try {
                 const resp = await fetch(fnUrl, {
                     method: "POST",
                     headers: {
                         "accept": "application/json",
                         "content-type": "application/json"
                     },
                     body: JSON.stringify({ url, approved })
                 });
                 const result = await resp.json();
                 console.log("Callback answer = ", result);
             } catch(e) {
                 console.log(e);
             }
         }

  4. Edit the `script.js` file, replacing the `UPDATE_ME` placeholders with the Cloud Run function URLs you noted previously.

     1. In the `translateBtn.addEventListener` method, replace `const fnUrl = UPDATE_ME;` with:  

            
            const fnUrl = "https://REGION-PROJECT_ID.cloudfunctions.net/invokeTranslationWorkflow";

     2. In the `callCallbackUrl` function, replace `const fnUrl = UPDATE_ME;` with:  

            
            const fnUrl = "https://REGION-PROJECT_ID.cloudfunctions.net/translationCallbackCall";

  5. Create a text file with the filename `style.css` that contains the following cascading styles:
         
         * {
             font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
         }
         
         body {
             margin: 20px;
         }
         
         h1, h2, h3, h4 {
             color: #0ea5e9;
         }
         




## Add Firebase to your web app

In this tutorial, the HTML page, JavaScript script, and CSS style sheet are deployed as static assets using Firebase Hosting but they can be hosted anywhere and served locally on your own machine for testing purposes.

### Create a Firebase project

Before you can add Firebase to your app, you need to create a Firebase project to connect to your app.

  1. In the [Firebase console](https://console.firebase.google.com), click **Create a project** , and then select your existing Google Cloud project from the drop-down menu to add Firebase resources to that project.

  2. Click **Continue** until you see the option to add Firebase.

  3. Skip setting up Google Analytics for your project.

  4. Click **Add Firebase**.




Firebase automatically provisions resources for your Firebase project. When the process completes, you'll be taken to the overview page for your project in the Firebase console.

### Register your app with Firebase

After you have a Firebase project, you can add your web app to it.

  1. In the center of the project overview page, click the **Web** icon (**< />**) to launch the setup workflow.

  2. Enter a nickname for your app.

This is only visible to you in the Firebase console.

  3. Skip setting up Firebase Hosting for now.

  4. Click **Register app** and continue to the console.




### Enable Cloud Firestore

The web app uses Cloud Firestore to receive and save data. You'll need to enable Cloud Firestore.

  1. In the Firebase console's **Build** section, click **Firestore Database**.

(You might have to first expand the left navigation pane to see the **Build** section.)

  2. In the Cloud Firestore pane, click **Create database**.

  3. Select **Start in test mode** , using a security rule like the following:
         
         rules_version = '2';
         service cloud.firestore {
         match /databases/{database}/documents {
           match /{document=**} {
             allow read, write;
           }
         }
         }

**Note:** Test mode ensures that you can freely write to the database during development. This is **not** recommended for a production application.
  4. Click **Next** after reading the disclaimer about the security rules.

  5. Set the location where your Cloud Firestore data is stored. You can accept the default or choose a region close to you.

  6. Click **Enable** to provision Firestore.




### Add the Firebase SDK and initialize Firebase

Firebase provides JavaScript libraries for most Firebase products. Before using Firebase Hosting, you must add the Firebase SDKs to your Web app.

  1. To initialize Firebase in your app, you need to provide your app's Firebase project configuration. 
     1. In the Firebase console, go to your **Project settings** settings.
     2. In the **Your apps** pane, select your app.
     3. In the **SDK setup and configuration** pane, to load Firebase SDK libraries from the CDN, select **CDN**.
     4. Copy the snippet to your `index.html` file at the bottom of the `<body>` tag, replacing the `XXXX` placeholder values.
  2. Install the Firebase JavaScript SDK.

     1. If you don't already have a `package.json` file, create one by running the following command from the `callback-translation` directory:
            
            npm init

     2. Install the `firebase` npm package and save it to your `package.json` file by running:
            
            npm install firebase




### Initialize and deploy your project

To connect your local project files to your Firebase project, you must initialize your project. You can then deploy your web app.

  1. From the `callback-translation` directory, run the following command:
         
         firebase init

  2. Select the `Configure files for Firebase Hosting and (optionally) set up GitHub Action deploys` option.

  3. Choose to use an existing project and enter your project ID.

  4. Accept `public` as the default public root directory.

  5. Choose to configure a single-page app.

  6. Skip setting up automatic builds and deploys with GitHub.

  7. At the `File public/index.html already exists. Overwrite?` prompt, type **No**.

  8. Change to the `public` directory:
         
         cd public

  9. From the `public` directory, run the following command to deploy your project to your site:
         
         firebase deploy --only hosting




## Test the web app locally

Firebase Hosting lets you [view and test changes locally](https://firebase.google.com/docs/hosting/test-preview-deploy) and interact with emulated backend project resources. When using `firebase serve`, your app interacts with an emulated backend for your hosting content and config but your real backend for all other project resources. For this tutorial, you can use `firebase serve` but it is not recommended when doing more extensive testing.

  1. From the `public` directory, run the following command:
         
         firebase serve

  2. Open your web app at the local URL returned (usually `http://localhost:5000`).

  3. Enter some text in English and then click **Translate**.

A translation of the text in French should be displayed.

  4. You can now click **Validate** or **Reject**.

In the Firestore database, you can verify the contents. It should resemble the following:
         
         approved: true
         callback: "https://workflowexecutions.googleapis.com/v1/projects/26811016474/locations/us-central1/workflows/translation_validation/executions/68bfce75-5f62-445f-9cd5-eda23e6fa693/callbacks/72851c97-6bb2-45e3-9816-1e3dcc610662_1a16697f-6d90-478d-9736-33190bbe222b"
         text: "The quick brown fox jumps over the lazy dog."
         translation: "Le renard brun rapide saute par-dessus le chien paresseux."
         

The `approved` status is `true` or `false` depending on whether you validate or reject the translation.




Congratulations! You have created a human-in-the-loop translation workflow that uses Workflows callbacks.

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

**Note:** You can delete your Firebase project but be aware that by doing so you also: 

  * Disable all Firebase services in use by the project
  * Disable all Google Cloud services and APIs in use by the project
  * Delete the project from the Firebase and Google Cloud consoles



### Delete tutorial resources

  1. Remove the gcloud CLI default configuration you added during the tutorial setup:
         
         gcloud config unset workflows/location

  2. Delete the workflow created in this tutorial:
         
         gcloud workflows delete WORKFLOW_NAME

  3. Delete the Cloud Run functions you created in this tutorial:
         
         gcloud functions delete FUNCTION_NAME

You can also delete Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/functions/list).




## What's next

  * [Wait for events using callbacks and Eventarc triggers](https://docs.cloud.google.com/workflows/docs/tutorials/create-wait-for-events-callbacks)
  * [Workflows overview](https://docs.cloud.google.com/workflows/docs/overview)
  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
