---
url: https://docs.cloud.google.com/app-lifecycle-manager/samples/alm-ui-sample/
title: UI sample \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:36.638445+00:00
---

# UI sample  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/samples/alm-ui-sample/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Samples ](https://docs.cloud.google.com/app-lifecycle-manager/samples)



#  UI sample Stay organized with collections  Save and categorize content based on your preferences. 

Samples related to UI with Application Lifecycle Management.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [App Lifecycle Manager quickstart using client libraries](https://docs.cloud.google.com/app-lifecycle-manager/docs/quickstart-client-libraries). For more information, see the [App Lifecycle Manager Python API reference documentation](https://googleapis.github.io/google-cloud-python/latest/translate/usage.html). 

To authenticate to App Lifecycle Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    import subprocess
    
    from flask import Flask, make_response, render_template, request
    import requests
    
    app = Flask(__name__)
    
    GCP_REGIONS = [
        "africa-south1",
        "asia-east1",
        "asia-east2",
        "asia-northeast1",
        "asia-northeast2",
        "asia-northeast3",
        "asia-south1",
        "asia-south2",
        "asia-southeast1",
        "asia-southeast2",
        "australia-southeast1",
        "australia-southeast2",
        "europe-central2",
        "europe-north1",
        "europe-southwest1",
        "europe-west1",
        "europe-west2",
        "europe-west3",
        "europe-west4",
        "europe-west6",
        "europe-west8",
        "europe-west9",
        "europe-west10",
        "europe-west12",
        "me-central1",
        "me-central2",
        "me-west1",
        "northamerica-northeast1",
        "northamerica-northeast2",
        "southamerica-east1",
        "southamerica-west1",
        "us-central1",
        "us-east1",
        "us-east4",
        "us-east5",
        "us-south1",
        "us-west1",
        "us-west2",
        "us-west3",
        "us-west4",
    ]
    
    
    # --- PAGE 1: Apigee Generate & Deploy ---
    @app.route("/", methods=["GET", "POST"])
    def generate_api():
        action_result = None
        error_message = None
    
        if request.method == "POST":
            # Get dynamic variables from the form
            apigee_org = request.form.get("apigee_org")
            revision = "12"  # request.form.get("revision")
            service_account = request.form.get("service_account")
    
            # Hardcoded variables
            apigee_env = "prod"
            apigee_api = "saas-runtime"
            zip_filename = f"{apigee_api}_rev{revision}.zip"
    
            try:
                # --- TOKEN GENERATION ---
                print("Generating gcloud token...")
                token_cmd = [
                    "gcloud",
                    "auth",
                    "print-access-token",
                    f"--impersonate-service-account={service_account}",
                ]
                token = subprocess.check_output(token_cmd, text=True).strip()
    
                headers = {"Authorization": f"Bearer {token}"}
    
                # --- STEP 1: Download ---
                print(f"Step 1: Downloading {apigee_api} revision {revision}...")
                download_url = (
                    f"https://apigee.googleapis.com/v1/organizations/{apigee_org}/"
                    f"apis/{apigee_api}/revisions/{revision}?format=bundle"
                )
                dl_response = requests.get(download_url, headers=headers)
                dl_response.raise_for_status()
    
                # Save the zip file locally
                with open(zip_filename, "wb") as f:
                    f.write(dl_response.content)
    
                # --- STEP 2: Import ---
                print("Step 2: Importing proxy bundle...")
                import_url = (
                    f"https://apigee.googleapis.com/v1/organizations/{apigee_org}/"
                    f"apis?name={apigee_api}&action=import"
                )
    
                # Open the file and send as multipart/form-data
                with open(zip_filename, "rb") as f:
                    files = {"file": (zip_filename, f, "application/zip")}
                    import_response = requests.post(
                        import_url, headers=headers, files=files
                    )
    
                import_response.raise_for_status()
                new_revision = import_response.json().get("revision")
                print(f"Imported successfully! New Apigee Revision: {new_revision}")
    
                # --- STEP 3: Deploy ---
                print(f"Step 3: Deploying revision {new_revision} to {apigee_env}...")
                deploy_url = (
                    f"https://apigee.googleapis.com/v1/organizations/{apigee_org}/"
                    f"environments/{apigee_env}/apis/{apigee_api}/revisions/{new_revision}/"
                    f"deployments?serviceAccount={service_account}&override=true"
                )
                deploy_response = requests.post(deploy_url, headers=headers)
                deploy_response.raise_for_status()
    
                # Clean up the local zip file
                if os.path.exists(zip_filename):
                    os.remove(zip_filename)
    
                action_result = (
                    f"Success! Revision {new_revision} of {apigee_api} "
                    f"deployed to {apigee_env}."
                )
    
                # Set a cookie just in case Page 2 needs to know what revision was created
                resp = make_response(
                    render_template("page1.html", action_result=action_result)
                )
                resp.set_cookie("last_deployed_revision", str(new_revision))
                return resp
    
            except subprocess.CalledProcessError:
                error_message = (
                    "Gcloud Token Error: Failed to impersonate service account. "
                    "Make sure gcloud is authenticated."
                )
            except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"
            except Exception as e:
                error_message = f"System Error: {str(e)}"
    
            # Clean up file if it failed halfway through
            if "zip_filename" in locals() and os.path.exists(zip_filename):
                os.remove(zip_filename)
    
        return render_template(
            "page1.html", action_result=action_result, error=error_message
        )
    
    
    # --- PAGE 2: GCP Region Selector ---
    @app.route("/deploy", methods=["GET", "POST"])
    def deploy_page():
        selected_region = None
        api_response_data = None
        operation_state = None
    
        if request.method == "POST":
            selected_region = request.form.get("region")
            action = request.form.get("action")
    
            if action == "deploy":
                url = "https://apigee.saas8384.saas-example.com/v1/saas/operations"
                headers = {"Content-Type": "application/json"}
                payload = {"region": selected_region}
    
                try:
                    response = requests.post(url, headers=headers, json=payload)
                    response.raise_for_status()
                    api_response_data = response.json()
                except requests.exceptions.RequestException as e:
                    api_response_data = {"error": str(e)}
    
            elif action == "status":
                operation_id = "depr-25094d41-7768-4ef3-bd8d-e5bf67ca09d6"
                url = (
                    f"https://apigee.saas8384.saas-example.com/v1/saas/operations/"
                    f"{operation_id}?region={selected_region}"
                )
    
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    operation_state = response.json().get("state", "STATE_UNKNOWN")
                except requests.exceptions.RequestException:
                    operation_state = "ERROR_FETCHING_STATE"
    
        return render_template(
            "page2.html",
            regions=GCP_REGIONS,
            selected_region=selected_region,
            api_response=api_response_data,
            operation_state=operation_state,
        )
    
    
    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 8080))
        app.run(host="0.0.0.0", port=port, debug=True)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=applifecyclemanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
