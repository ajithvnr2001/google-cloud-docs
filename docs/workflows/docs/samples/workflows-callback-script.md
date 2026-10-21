---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-callback-script/
title: Execute workflow for callback app \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:46.689255+00:00
---

# Execute workflow for callback app  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-callback-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Execute workflow for callback app Stay organized with collections  Save and categorize content based on your preferences. 

Web app to support a translation workflow that waits for human input and uses callback endpoints.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a human-in-the-loop workflow using callbacks](https://docs.cloud.google.com/workflows/docs/tutorials/callbacks-firestore)



## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
