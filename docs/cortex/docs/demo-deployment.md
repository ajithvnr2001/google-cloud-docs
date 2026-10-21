---
url: https://docs.cloud.google.com/cortex/docs/demo-deployment/
title: Demo deployment \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:59:10.236496+00:00
---

# Demo deployment  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/demo-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Demo deployment

The **demo deployment** offers a streamlined experience using a predefined raw sample-dataset. It provides an end-to-end workflow to deploy the Cortex Framework Dataform pipelines for orchestration and to initialize the corresponding BigQuery datasets with sample data.

**Caution:** The demo deployment is not suitable for production environments. For production deployments, see [Cortex Framework production deployment](https://docs.cloud.google.com/cortex/docs/deployment).

## Before you begin

Ensure you have completed the prerequisites outlined on the [Prerequisites](https://docs.cloud.google.com/cortex/docs/prerequisites) page, before continuing with the demo deployment.

## Get the required IAM roles and permissions

Obtain the required Identity and Access Management (IAM) permissions to deploy Cortex Framework content within the target Google Cloud project.

### Roles for target project

To get the permissions that you need to deploy Cortex Framework, ask your administrator to grant you the following IAM roles on your target project: 

  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** The Dataform Admin (`roles/dataform.admin`) privilege may be substituted with Dataform Editor (`roles/dataform.editor`) privilege, if the default Dataform repository `cortex-framework-demo` or repository specified using `--repository_name` [parameter](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-demo) has been created before the execution of the command `uv run cortex-demo`. Dataform repository creation can be triggered using the command: `curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '' "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/repositories?repositoryId=cortex-framework-demo"`

To grant the requested roles to a user, you can use the script:
    
    
    # Grant BigQuery JobUser to the user
    gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_EMAIL" \
            --role="roles/bigquery.jobUser"
    
    # Grant BigQuery DataEditor to the user
    gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_EMAIL" \
            --role="roles/bigquery.dataEditor"
    
    # Grant BigQuery Dataform admin to the user
    gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_EMAIL" \
            --role="roles/dataform.admin"
    
    # Grant Service Usage Consumer to the user
    gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_EMAIL" \
            --role="roles/serviceusage.serviceUsageConsumer"
    

## Optional: Get the required IAM roles for a demo deployment using a service account

The following roles are required only for a demo deployment with the optional `--service_account` parameter enabled. Providing a service account simplifies post-deployment tasks by setting up the scheduling of the data pipelines. You can manually trigger this workflow configuration in Dataform on the **Release and Scheduling** tab using the three-dot menu.

To get the permissions that you need to deploy the demo of Cortex Framework, ask your administrator to grant you the [Service Account Token Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role on your source and target project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To create the service account and grant the necessary roles, you can use the following script:
    
    
    # Create the service account
    gcloud iam service-accounts create cortex-dataform \
            --description="Service account for Cortex Dataform execution" \
            --display-name="Cortex Dataform Service Account" \
            --project=PROJECT_ID
    
    # Wait for the service account to propagate (IAM eventual consistency)
    sleep 10
    
    # Grant BigQuery DataEditor to the service account
    gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:cortex-dataform@PROJECT_ID.iam.gserviceaccount.com" \
            --role="roles/bigquery.dataEditor"
    
    # Grant BigQuery jobUser to the service account
    gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:cortex-dataform@PROJECT_ID.iam.gserviceaccount.com" \
            --role="roles/bigquery.jobUser"
    
    # Grant Dataform Editor to the service account
    gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:cortex-dataform@PROJECT_ID.iam.gserviceaccount.com" \
            --role="roles/dataform.editor"
    
    # Grant the user Service Account Token Creator role on the Cortex service account
    gcloud iam service-accounts add-iam-policy-binding \
            cortex-dataform@PROJECT_ID.iam.gserviceaccount.com \
            --member="user:USER_EMAIL" \
            --role="roles/iam.serviceAccountTokenCreator" \
            --project=PROJECT_ID
    
    PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
    
    ## Note: In case the commands below should fail with message: 
    # "serviceAccount:service-$PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com" not found
    # the default dataform service accounts hasn't been yet provisioned for given project.
    # In such case, please execute the commands after initial run of `uv run cortex-*`
    
    # Grant the Dataform Service Account the Token Creator role on the Cortex service account
    gcloud iam service-accounts add-iam-policy-binding \
            cortex-dataform@PROJECT_ID.iam.gserviceaccount.com \
            --member="serviceAccount:service-$PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com" \
            --role="roles/iam.serviceAccountTokenCreator" \
            --project=PROJECT_ID
    
    # Grant the Dataform Service Account the Service Account User role on the Cortex service account
    gcloud iam service-accounts add-iam-policy-binding \
            cortex-dataform@PROJECT_ID.iam.gserviceaccount.com \
            --member="serviceAccount:service-$PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com" \
            --role="roles/iam.serviceAccountUser" \
            --project=PROJECT_ID
    

## Deployment

Follow these steps to create a virtual Python environment, synchronize the dependencies, and trigger the data pipelines. Remember to use the Cortex Framework `uv` scripts to build and push your data assets to your Google Cloud project, transforming your local configurations into a live, scalable data architecture. For more information, see the [`uv` installation](https://docs.cloud.google.com/cortex/docs/prerequisites#install_uv) in the [Prerequisites](https://docs.cloud.google.com/cortex/docs/prerequisites) section.

### Execute the demo deployment

Run the following command to trigger the deployment. This process will perform the following actions:

  * Verify that all prerequisites are complete.
  * Load sample data into a BigQuery dataset to serve as the raw layer for demonstration purposes.
  * Build Dataform pipelines for processing the sample data through the Cortex Framework data layers.
  * Create the Dataform repository and workspace, then sync the compiled artifacts with the repository. *Optional: If Service Account has been provided with `--service_account` \- create workflow schedule and trigger the initial Dataform workflow execution.

**Note:** Running the `uv run cortex-demo` command collects anonymous telemetry data. For more information and instructions on how to opt out, see [Telemetry](https://docs.cloud.google.com/cortex/docs/telemetry).**Note:** **uv run cortex-demo CLI parameters** : you can optionally display a list of possible parameters supported by the cortex-demo script by running the `uv run cortex-demo -h` command. For more information and full list of available parameters see [CLI Cortex Framework demo deployment](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-demo).

For demo deployment with default values, execute the following command:
    
    
    uv run cortex-demo --project_id=PROJECT_ID --sap_version s4
    

For demo deployment with a service account, execute the following command:

**Note:** `--service_account` is an optional parameter.
    
    
    uv run cortex-demo --project_id=PROJECT_ID \
      --service_account="cortex-dataform@PROJECT_ID.iam.gserviceaccount.com" \
      --create_workflow_configs 
    

**Note:** For detailed information on monitoring deployment progress, pipeline execution, and data quality, see [Cortex Framework Observability](https://docs.cloud.google.com/cortex/docs/observability).

## Verification

Once the deployment completes:

  1. Open [Dataform](https://console.cloud.google.com/bigquery/dataform) to inspect the new code created in the repository:

     1. Created Dataform repository: `cortex-framework-demo`
     2. Inside of the Dataform repository the development workspace: `demo`
     3. Compiled and synchronised code (you can see the graph clicking on `Compiled graph`).
  2. Manual execution of Dataform actions:

     1. Open the Dataform workspace: "demo" from repository cortex-framework-demo in Google Cloud Dataform console.
     2. Click **Start execution**.
     3. Click **Execute actions**.
     4. Click **All actions**.
     5. Click **Start execution**.

     6. Monitor the successful execution of all actions in your Dataform repository using the tab: **Workflow Execution Logs**.

  3. Scheduled Dataform actions execution 




Applies only in case you have been using the `--service_account` and `--create_workflow_configs` parameters during deployment:

  1. Open the Dataform repository cortex-framework-demo in Google Cloud Dataform console.
  2. Click **Releases & scheduling**
  3. In section: **Workflow configurations** click the three-dot menu for action you are interested to execute and click **Start now**.

  4. Monitor the successful execution of all actions in your Dataform repository using the tab: **Workflow Execution Logs**.

  5. Navigate to the [BigQuery console](https://console.cloud.google.com/bigquery) and click `Datasets` to view the newly created datasets, and verify the schema and data. Created datasets:

     * `cortex_demo_sap_s4_raw`: This dataset contains the raw data from the source system (in this example, SAP S/4HANA).
     * `cortex_demo_sap_s4_data_foundation`: This dataset represents the data foundation layer, where raw data from the raw layer is CDC processed.
     * `cortex_demo_data_product`: This dataset contains the demo data products-refined, high-performance views or tables designed for end-user consumption.
     * `cortex_demo_samples`: This dataset contains the demo data for sample consumption data products.



## Cleanup demo deployment resources

After a successful demo deployment, you can remove the used Google Cloud resources to avoid ongoing charges. The following script deletes the created BigQuery datasets, the Dataform workspace, and the Dataform repository:
    
    
    #!/bin/bash
    
    # Define variables using names from uv-run-cortex-demo.md
    PROJECT_ID="PROJECT_ID"
    SAP_VERSION="s4"
    
    DATAFORM_REGION="us-central1"
    SOURCE_SAP_RAW_DATASET_ID="cortex_demo_sap_s4_raw"
    TARGET_SAP_FOUNDATION_DATASET_ID="cortex_demo_sap_s4_data_foundation"
    if [[ "$SAP_VERSION" == "ecc" ]]; then
      SOURCE_SAP_RAW_DATASET_ID="cortex_demo_sap_ecc_raw"
      TARGET_SAP_FOUNDATION_DATASET_ID="cortex_demo_sap_ecc_data_foundation"
    fi
    TARGET_DP_DATASET_ID="cortex_demo_data_product"
    TARGET_SAMPLES_DATASET_ID="cortex_demo_samples"
    REPOSITORY_NAME="cortex-framework-demo"
    WORKSPACE_NAME="demo"
    SERVICE_ACCOUNT_NAME="cortex-dataform"
    
    
    # Color codes for formatting status output
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    RED='\033[0;31m'
    NC='\033[0m' # No Color
    
    # Helper function to delete a resource and report status
    delete_resource() {
        local label=$1
        local url=$2
        local resource_type=$3
        
        echo -n "${label}... "
        
        local temp_file=$(mktemp)
        local code=$(curl -s -o "${temp_file}" -w "%{http_code}" -X DELETE \
            -H "Authorization: Bearer ${ACCESS_TOKEN}" \
            "${url}")
            
        if [ "$code" -eq 200 ] || [ "$code" -eq 204 ]; then
            echo -e "${GREEN}ok${NC}"
        elif [ "$code" -eq 404 ]; then
            echo -e "${YELLOW}skipped, ${resource_type} not found${NC}"
        else
            echo -e "${RED}failed (HTTP ${code})${NC}"
            if [ -s "${temp_file}" ]; then
                echo "  Error details:"
                sed 's/^/    /' "${temp_file}"
            fi
        fi
        rm -f "${temp_file}"
    }
    
    echo "Deleting BigQuery datasets..."
    for DATASET_ID in "${SOURCE_SAP_RAW_DATASET_ID}" \
                      "${TARGET_SAP_FOUNDATION_DATASET_ID}" \
                      "${TARGET_DP_DATASET_ID}" \
                      "${TARGET_SAMPLES_DATASET_ID}"; do
        echo "deleting ${PROJECT_ID}:${DATASET_ID}"
        bq rm -r -f "${PROJECT_ID}:${DATASET_ID}"
    done
    
    ACCESS_TOKEN=$(gcloud auth print-access-token)
    delete_resource "Deleting Dataform workspace ${WORKSPACE_NAME}" \
        "https://dataform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${DATAFORM_REGION}/repositories/${REPOSITORY_NAME}/workspaces/${WORKSPACE_NAME}" \
        "workspace"
    
    echo "Deleting Dataform workflow configurations..."
    WORKFLOW_CONFIGS_JSON=$(curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" \
        "https://dataform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${DATAFORM_REGION}/repositories/${REPOSITORY_NAME}/workflowConfigs")
    
    WORKFLOW_CONFIGS=$(echo "${WORKFLOW_CONFIGS_JSON}" | grep '"name":' | sed -E 's/.*"name": "([^"]+)".*/\1/')
    
    if [ -z "${WORKFLOW_CONFIGS}" ]; then
        echo -e "  No workflow configurations found. ${YELLOW}skipped${NC}"
    else
        for config in ${WORKFLOW_CONFIGS}; do
            delete_resource "  Deleting workflow config: ${config##*/}" \
                "https://dataform.googleapis.com/v1beta1/${config}" \
                "workflow config"
        done
    fi
    
    echo "Deleting Dataform release configurations..."
    RELEASE_CONFIGS_JSON=$(curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" \
        "https://dataform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${DATAFORM_REGION}/repositories/${REPOSITORY_NAME}/releaseConfigs")
    
    RELEASE_CONFIGS=$(echo "${RELEASE_CONFIGS_JSON}" | grep '"name":' | sed -E 's/.*"name": "([^"]+)".*/\1/')
    
    if [ -z "${RELEASE_CONFIGS}" ]; then
        echo -e "  No release configurations found. ${YELLOW}skipped${NC}"
    else
        for config in ${RELEASE_CONFIGS}; do
            delete_resource "  Deleting release config: ${config##*/}" \
                "https://dataform.googleapis.com/v1beta1/${config}" \
                "release config"
        done
    fi
    
    delete_resource "Deleting Dataform repository ${REPOSITORY_NAME}" \
        "https://dataform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${DATAFORM_REGION}/repositories/${REPOSITORY_NAME}?force=true" \
        "repository"
    
    if gcloud iam service-accounts describe "${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" --project="${PROJECT_ID}" >/dev/null 2>&1; then
        read -p "Do you want to delete the service account ${SERVICE_ACCOUNT_NAME}? (y/N): " -r
        if [[ "$REPLY" =~ ^[Yy]$ ]]; then
            echo -n "Deleting service account ${SERVICE_ACCOUNT_NAME}... "
            ERROR_MSG=$(gcloud iam service-accounts delete "${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" --project="${PROJECT_ID}" --quiet 2>&1)
            EXIT_CODE=$?
            if [ ${EXIT_CODE} -eq 0 ]; then
                echo -e "${GREEN}ok${NC}"
            else
                echo -e "${RED}failed${NC}"
                echo "  Error details:"
                echo "${ERROR_MSG}" | sed 's/^/    /'
            fi
        else
            echo -e "Deleting service account ${SERVICE_ACCOUNT_NAME}... ${YELLOW}skipped (user cancelled)${NC}"
        fi
    else
        echo -e "Deleting service account ${SERVICE_ACCOUNT_NAME}... ${YELLOW}skipped, service account not found${NC}"
    fi
    
    echo "Cortex Framework demo deployment cleanup complete."
    

## Next steps

  * **Follow the[Production deployment](https://docs.cloud.google.com/cortex/docs/deployment)** to learn how to deploy Google Cloud Cortex Framework in production environments.

  * **Read about[Source system integration](https://docs.cloud.google.com/cortex/docs/source-system-integration/overview)** to learn how to connect your production systems.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
