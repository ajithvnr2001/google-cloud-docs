---
url: https://docs.cloud.google.com/security-command-center/docs/configure-cicd-integration/
title: Configure CI/CD integration \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:13.177282+00:00
---

# Configure CI/CD integration  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/configure-cicd-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Configure CI/CD integration Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions.  Artifact guard and CI/CD integration will be shut down on October 30, 2026. 

The CI/CD integration connects your CI/CD pipelines to artifact guard to detect container vulnerabilities during the build stage.

The scanner supports GitHub Actions, [Cloud Build](https://docs.cloud.google.com/build/docs/overview), and Jenkins. When integrated into a pipeline, it evaluates container images against your artifact guard policies before the images are pushed to a registry.

## Scanner capabilities

The CI/CD integration runs as a binary within your CI/CD workflow to perform the following tasks:

  * **Build-time policy evaluation** : Scans newly built container images against your configured artifact guard policies.
  * **Build blocking** : Returns exit codes to your CI/CD runner (GitHub Actions, Cloud Build, or Jenkins) to block builds that violate your security policies.
  * **Scan reporting** : Sends vulnerability scan results to Security Command Center and outputs local reports in JSON or SARIF formats.



### Target roles and responsibilities

The CI/CD integration is designed for the following teams:

  * **DevOps or Platform Engineering teams** : Create pipeline connectors and add scanner execution steps to CI/CD workflow configurations.
  * **Security Administrators** : Define the build-time vulnerability policies that the scanner enforces.
  * **Application Developers** : Review scan execution logs in CI/CD build outputs to identify and fix policy violations.



### Key terms and concepts

  * **Common Vulnerabilities and Exposures (CVE)** : A publicly disclosed computer security vulnerability that is assigned a unique identifier.
  * **Software Bill of Materials (SBOM)** : A machine-readable inventory of software components and dependencies used to identify CVEs and other security risks.
  * **Artifact** : In the context of artifact guard, a container image built by a CI/CD pipeline.
  * **Connector** : A resource that links your CI/CD pipeline to artifact guard. When passed from the CI pipeline during a scan, the connector ID determines which policies evaluate the image.
  * **CI Policy** : A vulnerability policy defining the specific CVE, severity, and package rules enforced during CI/CD builds.



### High-level workflow

To configure and run CI/CD vulnerability scans, complete the following workflow:

  1. Create a CI connector for your target CI/CD platform.
  2. [Create an artifact guard policy](https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard) that includes the connector ID in its pipeline scope.
  3. Configure your CI/CD pipeline to authenticate to Google Cloud, build the container image, and run the scanner container.



When the pipeline runs, the scanner evaluates the container image against your policy. If the image violates the policy, the scanner returns a failure exit code to fail the build. Developers can then inspect the build logs, update vulnerable dependencies, and rerun the build.

## Before you begin

To use the CI/CD integration, you must enable artifact guard. For instructions, see [Before you begin](https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard#before-you-begin) in the artifact guard documentation.

## Create a connector

### Console

To create a connector in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to **Security > Settings**.
  2. On the **Artifact guard** card, click **Manage settings**.
  3. Click **Create connector** and enter the following details for the connector: 
     * **Connector ID** : Add an ID for the connector.
     * **Description** : Enter a description of the connector.
     * **CI/CD platform** : Select the corresponding CI/CD platform from the list. Use this connector only in pipelines built with the selected CI/CD platform.
  4. Click **Create**.



A notification confirms successful connector creation. The **Connectors** table lists available connectors.

### gcloud CLI

To create a connector using the gcloud CLI, run the following command:
    
    
    gcloud alpha scc artifact-guard connectors create CONNECTOR_ID \
        --location=LOCATION \
        (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER) \
        --pipeline-type=PIPELINE_TYPE \
        [--description=DESCRIPTION] \
        [--display-name=DISPLAY_NAME]

Replace the following:

  * CONNECTOR_ID: An identifier for the connector (for example, `my-connector`).
  * LOCATION: The Security Command Center location where your data is stored. Only `global` is supported.
  * ORGANIZATION_ID: The organization ID.
  * PROJECT_NUMBER: The numeric project number.
  * PIPELINE_TYPE: The type of CI/CD pipeline. Must be one of the following: 
    * `GOOGLE_CLOUD_BUILD`
    * `GITHUB_ACTIONS`
    * `JENKINS_PIPELINE`
  * DESCRIPTION: A text description for the connector.
  * DISPLAY_NAME: A user-friendly display name for the connector.



## Update a connector

### Console

To link a policy to a connector in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to **Security > Settings**.
  2. On the **Artifact guard** card, click **Manage settings**.
  3. In the **Connectors** table, click more_vert next to the connector and select **Add policy**.
  4. Proceed with the steps to create or update an artifact guard policy. For more information, see [Create a policy](https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard#create-policy).



### gcloud CLI

To view existing connectors and update their policy associations using the gcloud CLI, use the following commands:

#### List connectors
    
    
    gcloud alpha scc artifact-guard connectors list PARENT

Replace the following:

  * PARENT: An organization or project. Acceptable formats for the parent resource include: 
    * `organizations/ORGANIZATION_ID/locations/LOCATION`
    * `projects/PROJECT_NUMBER/locations/LOCATION`



#### Describe a connector
    
    
    gcloud alpha scc artifact-guard connectors describe CONNECTOR_ID \
        --location=LOCATION \
        (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER)

#### Update connector policy association

To link a connector to a policy, include the connector ID in the pipeline scope of your policy definition file and update the policy using the `gcloud alpha scc artifact-guard policies update` command. For more information, see [Create a policy](https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard#create-policy).

## Delete a connector

### Console

To delete a connector in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to **Security > Settings**.
  2. On the **Artifact guard** card, click **Manage settings**.
  3. In the **Connectors** table, click more_vert next to the connector and select **Delete connector**.
  4. Follow the confirmation prompts to delete the connector. Click **Cancel** to abort.



### gcloud CLI

To delete a connector using the gcloud CLI, run the following command:
    
    
    gcloud alpha scc artifact-guard connectors delete CONNECTOR_ID \
        --location=LOCATION \
        (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER)

## Run an evaluation

GitHub Actions and Jenkins pipelines support vulnerability scanning. To perform an evaluation, you must do the following:

  1. Create secrets for authentication.
  2. Create an integration template file specific to your pipeline.
  3. Initiate an evaluation.



### Secret configuration

CI/CD pipelines running outside of Google Cloud can authenticate using either service account keys or Workload Identity Federation. For detailed instructions on creating secrets, see the following:

**Service account keys**

  * [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating)



**Workload Identity Federation** (for GitHub Actions)

  * [Configuring OpenID Connect in Google Cloud](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-google-cloud-platform)

  * <https://github.com/google-github-actions/auth>




You must add secrets to your CI/CD environment using one of the following methods:

**Service account key method**

One secret:

  * `GCP_CREDENTIALS`: The contents of your downloaded service account JSON key file.



**Workload Identity Federation method**

Two secrets:

  * `GCP_WORKLOAD_IDENTITY_PROVIDER`: The full resource name of your Workload Identity Provider. For example, `projects/12345/locations/global/workloadIdentityPools/my-pool/providers/my-provider`.

  * `GCP_SERVICE_ACCOUNT`: The email address of the service account to impersonate.




### Pipeline integration templates

To trigger an evaluation, you must create a file specific to your pipeline (Cloud Build, GitHub Actions or Jenkins) using the following template examples:

###  Cloud Build 

  * See Variable definitions for information about each field.
        
        steps:
              # Step 1: Generate auth token
              - name: 'gcr.io/cloud-builders/gcloud'
              id: 'Generate Token'
              entrypoint: 'bash'
              args:
                    - '-c'
                    - |
                    echo "Starting token generation..."
                    gcloud auth print-access-token > /workspace/gcp_token.txt
                    if [ $? -eq 0 ]; then
                          echo "Token generated successfully."
                    else
                          echo "Failed to generate token." >&2
                          exit 1
                    fi
        
              # Step 2: Build the image locally
              - name: 'gcr.io/cloud-builders/docker'
              id: 'Build Image'
              entrypoint: 'bash'
              args:
                    - '-c'
                    - |
                    echo "🚧 Building Docker image from source code..."
                    docker build -t ${_IMAGE_NAME_TO_SCAN}:${_IMAGE_TAG} .
                    if [ $? -ne 0 ]; then
                          echo "❌ Docker build failed."
                          exit 1
                    fi
                    echo "✅ Docker image built successfully: ${_IMAGE_NAME_TO_SCAN}:${_IMAGE_TAG}"
        
              # Step 3: Image scan for vulnerabilities
              - id: 'Image-Analysis'
              name: '${_SCANNER_IMAGE}'
              entrypoint: 'bash'
              args:
                    - '-c'
                    - |
                    echo "Starting image scan with scanner: ${_SCANNER_IMAGE}"
        
                    exit_code=0
        
                    docker run --rm \
                          -v /var/run/docker.sock:/var/run/docker.sock \
                          -v /workspace:/workspace \
                          -e GCP_PROJECT_ID="${_PROJECT_ID}" \
                          -e ORGANIZATION_ID="${_ORGANIZATION_ID}" \
                          -e IMAGE_NAME="${_IMAGE_NAME_TO_SCAN}" \
                          -e IMAGE_TAG="${_IMAGE_TAG}" \
                          -e CONNECTOR_ID="${_CONNECTOR_ID}" \
                          -e TRIGGER_ID="${_TRIGGER_ID}" \
                          -e IGNORE_ERRORS="${_IGNORE_ERRORS}" \
                          -e GCP_ACCESS_TOKEN="$(cat /workspace/gcp_token.txt)" \
                          "${_SCANNER_IMAGE}" || exit_code=$?
        
                    echo "Docker run finished with exit code: $exit_code"
        
                    if [ $exit_code -eq 0 ]; then
                          echo "✅ Evaluation succeeded: Conformant image."
                    elif [ $exit_code -eq 1 ]; then
                          echo "❌ Scan failed: Non-conformant image."
                          exit 1
                    else
                          if [ "${_IGNORE_ERRORS}" = "true" ]; then
                                echo "⚠️ Server/internal error ignored. Continuing."
                          else
                                echo "❌ Server/internal error. Exiting."
                                exit 1
                          fi
                    fi
        
              # Step 4: Configure Docker authentication for Artifact Registry
              - name: 'gcr.io/cloud-builders/gcloud'
              id: 'Configure Docker Auth'
              entrypoint: 'bash'
              args:
                    - '-c'
                    - |
                    echo "🔐 Configuring Docker authentication for Artifact Registry..."
                    gcloud auth configure-docker us-east1-docker.pkg.dev -q
                    echo "✅ Docker authentication configured."
        
              # Step 5: Push image to Artifact Registry
              - name: 'gcr.io/cloud-builders/docker'
              id: 'Push Image to Artifact Registry'
              entrypoint: 'bash'
              args:
                    - '-c'
                    - |
        
                    docker tag "${_IMAGE_NAME_TO_SCAN}:${_IMAGE_TAG}" "us-east1-docker.pkg.dev/${_PROJECT_ID}/${_AR_REPOSITORY}/${_IMAGE_NAME_TO_SCAN}:${_IMAGE_TAG}"
        
                    echo "🚀 Pushing $_FULL_AR_TAG..."
                    docker push "us-east1-docker.pkg.dev/${_PROJECT_ID}/${_AR_REPOSITORY}/${_IMAGE_NAME_TO_SCAN}:${_IMAGE_TAG}"
        
                    echo "✅ Image pushed successfully."
        
        substitutions:
              _IMAGE_NAME_TO_SCAN: 'checkout-image'
              _ORGANIZATION_ID: 'orgId'
              _CONNECTOR_ID: 'connectorId'
              _SCANNER_IMAGE: 'us-central1-docker.pkg.dev/ci-plugin/ci-images/scc-artifactguard-scan-image:latest'
              _IMAGE_TAG: 'latest'
              _TRIGGER_ID: 'cloud-build-job'
              _PROJECT_ID: 'projectId'
              _AR_REPOSITORY: 'images'
              _IGNORE_ERRORS: "false"
        
        serviceAccount: "projects/projectId/serviceAccounts/id-compute@developer.gserviceaccount.com"
        
        options:
              logging: CLOUD_LOGGING_ONLY
        




###  GitHub Actions (secret) 

This template is for GitHub Actions using a secret key.

  * Add your service account secret key (`GCP_CREDENTIALS`).
  * See Variable definitions for information about additional fields.
        
        # A workflow to BUILD the app image, RUN the scanner, and PUSH to AR if scan passes
        name: Build, Scan and Push
        
        on:
         workflow_dispatch:
           inputs:
              IMAGE_NAME_TO_SCAN:
                    description: 'The tag for your application image to be built (e.g., my-app:latest)'
                    required: true
                    default: 'checkout-image'
              GCP_PROJECT_ID:
                    description: 'GCP Project ID for authentication'
                    required: true
                    default: 'projectId'
              AR_REPOSITORY:
                    description: 'Artifact Registry repository name (e.g., app-repo)'
                    required: false
                    default: 'images'
              ORGANIZATION_ID:
                    description: 'Your GCP Organization ID'
                    required: true
                    default: 'orgId'
              CONNECTOR_ID:
                    description: 'The ID for your pipeline connector'
                    required: true
                    default: 'connectorId'
              SCANNER_IMAGE:
                    description: 'The full registry path for your PRE-BUILT scanner tool'
                    required: true
                    default: 'us-central1-docker.pkg.dev/ci-plugin/ci-images/scc-artifactguard-scan-image:latest'
              IMAGE_TAG:
                    description: 'The Docker image version (of the app image)'
                    required: true
                    default: 'latest'
              IGNORE_SERVER_ERRORS:
                    description: 'Ignore server errors'
                    required: false
                    type: boolean
                    default: false
              VERBOSITY:
                    description: 'Verbosity flag'
                    required: false
                    default: 'HIGH'
        
        jobs:
         build-and-scan:
           runs-on: ubuntu-latest
           steps:
              # 1. Check out repository (for your app's Dockerfile)
              - name: Check out repository
                uses: actions/checkout@v4
        
              # 2. Authenticate to Google Cloud
              - name: Authenticate to GCP
                id: auth
                uses: 'google-github-actions/auth@v2'
                with:
                    credentials_json: '${{ secrets.GCP_CREDENTIALS }}'
        
              # 3. Set up the gcloud CLI
              - name: Set up Cloud SDK
                uses: 'google-github-actions/setup-gcloud@v2'
                with:
                    project_id: ${{ inputs.GCP_PROJECT_ID }}
        
               # 4. Configure Docker (needed to pull SCANNER_IMAGE and push app image)
              - name: Configure Docker
                run: gcloud auth configure-docker us-central1-docker.pkg.dev --quiet
        
              # 5. Build Application Image Locally (IMAGE_NAME_TO_SCAN)
              - name: Build Application Image Locally
                uses: docker/build-push-action@v5
                with:
                    context: .
                    file: ./Dockerfile
                    push: false  # <-- Do not push
                    load: true   # <-- Load image into the runner's local daemon
                    # Tag the image with the name the scanner will look for
                    tags: |
                    ${{ inputs.IMAGE_NAME_TO_SCAN }}:${{ inputs.IMAGE_TAG }}
        
              # 6. Run Image Scan (Using the SCANNER_IMAGE)
              - name: 'Run Image Analysis Scan'
                if: steps.auth.outcome == 'success'
                run: |
                    echo "📦 Pulling scanner image and running scan..."
        
              SCANNER_IMAGE="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.SCANNER_IMAGE || env.SCANNER_IMAGE }}"
              GCP_PROJECT_ID="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.GCP_PROJECT_ID || env.GCP_PROJECT_ID }}"
              ORGANIZATION_ID="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.ORGANIZATION_ID || env.ORGANIZATION_ID }}"
              IMAGE_NAME="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.IMAGE_NAME_TO_SCAN || env.IMAGE_NAME_TO_SCAN }}"
              IMAGE_TAG="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.IMAGE_TAG || env.IMAGE_TAG }}"
              CONNECTOR_ID="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.CONNECTOR_ID || env.CONNECTOR_ID }}"
              VERBOSITY="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.VERBOSITY || env.VERBOSITY }}"
              IGNORE_ERRORS="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.IGNORE_SERVER_ERRORS || (env.IGNORE_SERVER_ERRORS == 'true') }}"
        
              exit_code=0
        
              # This 'docker run' pulls the SCANNER_IMAGE from the registry
              # and passes the name of the locally-built app image (IMAGE_NAME)
              docker run --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v ${{ steps.auth.outputs.credentials_file_path }}:/tmp/scc-key.json \
                    -e GCLOUD_KEY_PATH=/tmp/scc-key.json \
                    -e GCP_PROJECT_ID="${GCP_PROJECT_ID}" \
                    -e ORGANIZATION_ID="${ORGANIZATION_ID}" \
                    -e IMAGE_NAME="${IMAGE_NAME}" \
                    -e IMAGE_TAG="${IMAGE_TAG}" \
                    -e CONNECTOR_ID="${CONNECTOR_ID}" \
                    -e BUILD_TAG="${{ github.workflow }}" \
                    -e BUILD_ID="${{ github.run_number }}" \
                    -e VERBOSITY="${VERBOSITY}" \
                    "${SCANNER_IMAGE}" \
                    || exit_code=$?
        
              echo "Docker run finished with exit code: $exit_code"
        
              # --- Replicate Jenkins Exit Code Logic ---
              if [ $exit_code -eq 0 ]; then
                echo "✅ Evaluation succeeded: Conformant image."
              elif [ $exit_code -eq 1 ]; then
                echo "❌ Scan failed: Non-conformant image (vulnerabilities found)."
                exit 1 # Fail the step
              else
               if [ "$IGNORE_ERRORS" = "true" ]; then
                    echo "⚠️ Server/internal error occurred (Code: $exit_code), but IGNORE_SERVER_ERRORS=true. Proceeding."
              else
                echo "❌ Server/internal error occurred (Code: $exit_code) during evaluation. Set IGNORE_SERVER_ERRORS=true to override."
                exit 1 # Fail the step
              fi
              fi
        
              # 8. Push Application Image (ONLY if scan succeeded)
              # This step only runs if the 'Run Image Analysis Scan' step above exited with 0
              - name: Push Application Image to Artifact Registry
                run: |
                # Define the local and remote tags
                LOCAL_IMAGE_NAME="${{ inputs.IMAGE_NAME_TO_SCAN }}:${{ inputs.IMAGE_TAG }}"
        
                # This path is based on your 'Configure Docker' step (us-central1)
                # and the new AR_REPOSITORY input.
                FULL_AR_TAG="us-central1-docker.pkg.dev/${{ inputs.GCP_PROJECT_ID }}/${{ inputs.AR_REPOSITORY }}/${{ inputs.IMAGE_NAME_TO_SCAN }}:${{ inputs.IMAGE_TAG }}"
        
                echo "Tagging local image ${LOCAL_IMAGE_NAME} as ${FULL_AR_TAG}"
                docker tag "${LOCAL_IMAGE_NAME}" "${FULL_AR_TAG}"
        
                echo "Pushing ${FULL_AR_TAG} to Artifact Registry..."
                docker push "${FULL_AR_TAG}"
        




###  GitHub Actions (WIF) 

This template is for GitHub Actions using Workload Identity Federation.

  * Add your Workload Identity Provider in GitHub secret (`GCP_WORKLOAD_IDENTITY_PROVIDER`).
  * Add your Service Account in GitHub secret (`GCP_SERVICE_ACCOUNT`).
  * See Variable definitions for information about additional fields.
        
        # A workflow to BUILD the app image, RUN the scanner, and PUSH to AR if scan passes
        name: Build, Scan and Push
        
        on:
          push:
            branches:
              - main
          workflow_dispatch:
          inputs:
            IMAGE_NAME_TO_SCAN:
              description: 'The tag for your application image to be built (e.g., my-app:latest)'
              required: true
              default: 'checkout-image'
            GCP_PROJECT_ID:
              description: 'GCP Project ID for authentication and configuration'
              required: true
              default: 'projectId'
            ORGANIZATION_ID:
              description: 'Your GCP Organization ID'
              required: true
              default: 'orgId'
            CONNECTOR_ID:
              description: 'The ID for your pipeline connector'
              required: true
              default: 'connectorId'
            SCANNER_IMAGE:
              description: 'The Docker image that contains your scanner script'
              required: true
              default: 'us-central1-docker.pkg.dev/ci-plugin/ci-images/scc-artifactguard-scan-image:latest'
            IMAGE_TAG:
              description: 'The Docker image version'
              required: true
              default: 'latest'
            IGNORE_SERVER_ERRORS:
              description: 'If true, the pipeline continues on server/internal scanner errors.'
              required: false
              type: boolean
              default: false
        
        jobs:
          image-analysis-job:
          runs-on: ubuntu-latest
          permissions:
              contents: 'read'
              id-token: 'write'
        
          env:
              IMAGE_NAME_TO_SCAN: 'webgoat/webgoat'
              GCP_PROJECT_ID: 'projectId'
              ORGANIZATION_ID: 'orgId'
              CONNECTOR_ID: 'connectorId'
              SCANNER_IMAGE: 'us-central1-docker.pkg.dev/ci-plugin/ci-images/scc-artifactguard-scan-image:latest'
              IMAGE_TAG: 'imageTag'
              IGNORE_SERVER_ERRORS: 'false'
        
          steps:
              # Step 1: Authenticate and create credential file
              - name: 'Authenticate to Google Cloud'
              id: 'auth'
              uses: 'google-github-actions/auth@v2'
              with:
              workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
              service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}
              create_credentials_file: true
        
              # Step 2: Set up gcloud SDK
              - name: 'Set up gcloud SDK'
              uses: 'google-github-actions/setup-gcloud@v2'
        
              # Step 3: Configure Docker for registries
              - name: 'Configure Docker for Artifact Registry'
              run: |
              gcloud auth configure-docker us-central1-docker.pkg.dev --quiet
        
              # Step 4: Run Image Analysis Scan and Handle Exit Codes
              - name: 'Run Image Analysis Scan'
              run: |
              echo "📦 Running container from scanner image..."
        
              # Determine values: Use manual inputs if available (event_name=workflow_dispatch), otherwise use env defaults
              SCANNER_IMAGE="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.SCANNER_IMAGE || env.SCANNER_IMAGE }}"
              GCP_PROJECT_ID="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.GCP_PROJECT_ID || env.GCP_PROJECT_ID }}"
              ORGANIZATION_ID="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.ORGANIZATION_ID || env.ORGANIZATION_ID }}"
              IMAGE_NAME="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.IMAGE_NAME_TO_SCAN || env.IMAGE_NAME_TO_SCAN }}"
              IMAGE_TAG="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.IMAGE_TAG || env.IMAGE_TAG }}"
              CONNECTOR_ID="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.CONNECTOR_ID || env.CONNECTOR_ID }}"
              IGNORE_ERRORS="${{ github.event_name == 'workflow_dispatch' && github.event.inputs.IGNORE_SERVER_ERRORS || (env.IGNORE_SERVER_ERRORS == 'true') }}"
        
              # Variable to store exit code
              exit_code=0
        
              # Run docker and capture exit code using || trick
              docker run --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v ${{ steps.auth.outputs.credentials_file_path }}:/gcp-creds.json \
                    -e GOOGLE_APPLICATION_CREDENTIALS=/gcp-creds.json \
                    -e GCP_PROJECT_ID="${GCP_PROJECT_ID}" \
                    -e ORGANIZATION_ID="${ORGANIZATION_ID}" \
                    -e IMAGE_NAME="${IMAGE_NAME}" \
                    -e IMAGE_TAG="${IMAGE_TAG}" \
                    -e CONNECTOR_ID="${CONNECTOR_ID}" \
                    -e RUN_ID="${{ github.run_number }}" \
                    "${SCANNER_IMAGE}" \
                    || exit_code=$?
        
              echo "Docker run finished with exit code: $exit_code"
        
              if [ $exit_code -eq 0 ]; then
                    echo "✅ Evaluation succeeded: Conformant image."
              elif [ $exit_code -eq 1 ]; then
                    echo "❌ Scan failed: Non-conformant image (vulnerabilities found)."
                    exit 1 # Fail the step
              else
                    if [ "$IGNORE_ERRORS" = "true" ]; then
                    echo "⚠️ Server/internal error occurred (Code: $exit_code), but IGNORE_SERVER_ERRORS=true. Proceeding."
                    # Do nothing, step passes
                    else
                    echo "❌ Server/internal error occurred (Code: $exit_code) during evaluation. Set IGNORE_SERVER_ERRORS=true to override."
                    exit 1 # Fail the step
                    fi
              fi
        




###  Jenkins (secret) 

  * Add service account secret key (`GCP_CREDENTIALS`).
  * See Variable definitions for information about additional fields.
        
        pipeline {
              agent any
        
              parameters {
                    string(
                          name: 'IMAGE_NAME_TO_SCAN',
                          defaultValue: 'checkout-image',
                          description: 'The tag for your application image to be built (e.g., my-app:latest)'
                    )
                    string(
                          name: 'GCP_PROJECT_ID',
                          defaultValue: 'projectId',
                          description: 'GCP Project ID for authentication'
                    )
                    string(
                          name: 'AR_REPOSITORY',
                          defaultValue: 'images',
                          description: 'Artifact Registry repository name (e.g., app-repo)'
                    )
                    string(
                          name: 'ORGANIZATION_ID',
                          defaultValue: 'orgId',
                          description: 'Your GCP Organization ID'
                    )
                    string(
                          name: 'CONNECTOR_ID',
                          defaultValue: 'connectorId',
                          description: 'The ID for your pipeline connector'
                    )
                    string(
                          name: 'SCANNER_IMAGE',
                          defaultValue: 'us-central1-docker.pkg.dev/ci-plugin/ci-images/scc-artifactguard-scan-image:latest',
                          description: 'The full registry path for your PRE-BUILT scanner tool'
                    )
                    string(
                          name: 'IMAGE_TAG',
                          defaultValue: 'latest',
                          description: 'The Docker image version (of the app image)'
                    )
                    booleanParam(
                          name: 'IGNORE_SERVER_ERRORS',
                          defaultValue: false,
                          description: 'Ignore server errors'
                    )
                    string(
                          name: 'VERBOSITY',
                          defaultValue: 'HIGH',
                          description: 'Verbosity flag'
                    )
              }
        
        stages {
              // Stage 1: Check out the source code
              stage('Checkout') {
                    steps {
                    echo "Checking out source code..."
                    checkout scm
                    }
              }
        
              // Stage 2: Build application image
              stage('Build Application Image') {
                    steps {
                    echo "Building application image: ${params.IMAGE_NAME_TO_SCAN}:${params.IMAGE_TAG}"
                    sh "docker build -t ${params.IMAGE_NAME_TO_SCAN}:${params.IMAGE_TAG} -f ./Dockerfile ."
                    }
              }
        
              // Stage 3: Authenticate to Google Cloud and run scanner
              stage('Scan Image') {
                    steps {
                    script {
                          withCredentials([file(credentialsId: 'GCP_CREDENTIALS', variable: 'GCP_KEY_FILE')]) {
                                // Authenticate
                                sh "gcloud auth activate-service-account --key-file=\"$GCP_KEY_FILE\""
                                sh 'gcloud auth list'
                                sh 'gcloud auth configure-docker gcr.io --quiet'
                                sh 'gcloud auth configure-docker us-central1-docker.pkg.dev --quiet'
        
                                // Run scanner container
                                def exitCode = sh(
                                script: """
                                      echo "📦 Running scanner container from image: ${params.SCANNER_IMAGE}"
        
                                      docker run --rm \\
                                            -v /var/run/docker.sock:/var/run/docker.sock \\
                                            -v "$GCP_KEY_FILE":/tmp/scc-key.json \\
                                            -e GCLOUD_KEY_PATH=/tmp/scc-key.json \\
                                            -e GCP_PROJECT_ID="${params.GCP_PROJECT_ID}" \\
                                            -e ORGANIZATION_ID="${params.ORGANIZATION_ID}" \\
                                            -e IMAGE_NAME="${params.IMAGE_NAME_TO_SCAN}" \\
                                            -e IMAGE_TAG="${params.IMAGE_TAG}" \\
                                            -e CONNECTOR_ID="${params.CONNECTOR_ID}" \\
                                            -e BUILD_TAG="${env.JOB_NAME}" \\
                                            -e BUILD_ID="${env.BUILD_NUMBER}" \\
                                            "${params.SCANNER_IMAGE}"
                                """,
                                returnStatus: true
                                )
        
                                if (exitCode == 0) {
                                echo "✅ Evaluation succeeded: Conformant image."
                                } else if (exitCode == 1) {
                                error("❌ Scan failed: Non-conformant image (vulnerabilities found).")
                                } else {
                                if (params.IGNORE_SERVER_ERRORS) {
                                      echo "⚠️ Server/internal error occurred, but IGNORE_SERVER_ERRORS=true. Proceeding with pipeline."
                                } else {
                                      error("❌ Server/internal error occurred during evaluation. Set IGNORE_SERVER_ERRORS=true to override.")
                                }
                                }
                          }
                    }
                    }
              }
        
              // Stage 4: Push Application Image
              stage('Push Application Image') {
                    steps {
                    script {
                          def localImage = "${params.IMAGE_NAME_TO_SCAN}:${params.IMAGE_TAG}"
                          def remoteTag = "us-central1-docker.pkg.dev/${params.GCP_PROJECT_ID}/${params.AR_REPOSITORY}/${params.IMAGE_NAME_TO_SCAN}:${params.IMAGE_TAG}"
        
                          echo "Tagging local image ${localImage} as ${remoteTag}"
                          sh "docker tag ${localImage} ${remoteTag}"
        
                          echo "Pushing ${remoteTag} to Artifact Registry..."
                          sh "docker push ${remoteTag}"
                    }
                    }
              }
        }
        




### Variable definitions

This section provides information about the variable fields used in the Pipeline integration templates.

`IMAGE_NAME_TO_SCAN` (Required)

  * Specifies the tag of the application image to be built.



`GCP_PROJECT_ID` (Required)

  * Specifies the Google Cloud Project ID used for authentication and configuration.



`AR_REPOSITORY` (Optional)

  * Specifies the name of the Artifact Registry repository where the pipeline publishes the image if the build succeeds.



`ORGANIZATION_ID` (Required)

  * The Google Cloud organization ID.



`CONNECTOR_ID` (Required)

  * Specifies the connector ID of the pipeline to be used.



`SCANNER_IMAGE` (Required)

  * The prebuilt scanner image analyzes code, identifies vulnerabilities by evaluating images against policies during the build, and produces a conformance result to determine whether the CI/CD pipeline passes or fails.

Image details: `us-central1-docker.pkg.dev/ci-plugin/ci-images/scc-artifactguard-scan-image:latest`




`VERBOSITY` (Optional)

  * The scanner supports an optional `VERBOSITY` flag that controls the level of detail displayed in the scan output. The scanner output varies based on the verbosity level and conformance result (Pass or Fail).
  * The verbosity flag can be set to `LOW` or `HIGH`. It defaults to `LOW` if not provided.




###  Low verbosity (concise) 

**ArtifactGuard Conformance: Pass**

  * Details the policy names.
  * Provides only the summarized count of CVEs by severity.



**ArtifactGuard Conformance: Fail**

  * Details the reason for failure.
  * Lists only the specific CVEs that caused the failure.
  * Provides a summarized count of CVEs categorized by severity.



###  High verbosity (detailed) 

Provides a comprehensive list of all vulnerabilities found.

**ArtifactGuard Conformance: Pass**

  * Provides a list of all CVEs detected for the policy.
  * Provides a summary count of CVEs broken down by severity.
  * Provides a comprehensive list of all detected vulnerabilities.



**ArtifactGuard Conformance: Fail**

  * Includes the reason for failure.
  * Lists the CVEs causing the failure.
  * Provides a list of all CVEs detected for the policy.
  * Provides a summary count of CVEs broken down by severity.
  * Provides a comprehensive list of all detected vulnerabilities.



`IGNORE_SERVER_ERRORS` (Optional)

  * An optional boolean flag. If `true`, the pipeline continues despite server errors. Defaults to `false`.



### Initiate an evaluation

During the build process, a Docker-based strategy evaluates the image against predefined policies. The vulnerability scanning logic is contained within the `us-central1-docker.pkg.dev/ci-plugin/ci-images/scc-artifactguard-scan-image:latest` image.

To initiate a vulnerability scan in your CI/CD pipeline, run the following command:
    
    
    docker run --rm \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v ${{ steps.auth.outputs.credentials_file_path }}:/gcp-creds.json \
        -e GOOGLE_APPLICATION_CREDENTIALS=/gcp-creds.json \
        -e GCP_PROJECT_ID="${GCP_PROJECT_ID}" \
        -e ORGANIZATION_ID="${ORGANIZATION_ID}" \
        -e IMAGE_NAME="${IMAGE_NAME}" \
        -e IMAGE_TAG="${IMAGE_TAG}" \
        -e CONNECTOR_ID="${CONNECTOR_ID}" \
        -e RUN_ID="${{ github.run_number }}" \
        "${SCANNER_IMAGE}" \
        || exit_code=$?
    

The CI/CD integration propagates the Docker container's exit codes to the Jenkins or GitHub Actions runtime, which then determines the pipeline's pass or fail state.

## Troubleshooting

This section outlines common errors along with how to resolve them.

### CreateConnector failures

**Field** | **Required/Optional** | **Constraints**  
---|---|---  
`name` | Required | **Format:** Must match the regular expression [a-zA-Z0-9\\\\-\\\s_]+$  
Match one or more of the following: 

  * letters (uppercase or lowercase)
  * digits
  * hyphen -
  * whitespace (\s)
  * underscore _

  
  
**Max Length:** 64 characters.  
`pipeline_type` | Required | Must be one of the following enum values: 

  * `JENKINS_PIPELINE`
  * `GITHUB_ACTIONS`
  * `GOOGLE_CLOUD_BUILD`

  
`description` | Optional | Must not exceed 256 characters.  
`display_name` | Optional | Must not exceed 256 characters.  
  
### Other errors

The following table outlines some common errors and how to resolve them.

**Error Message** | **Cause** | **Action/Resolution**  
---|---|---  
Permission `artifactscanguard.connectors.create` denied on resource  | The user or service account lacks the `artifactscanguard.connectors.create` IAM permission on the resource (project, folder, or organization). | Grant the caller an IAM role that includes the `artifactscanguard.connectors.create` permission.  
`status.ErrFailedPrecondition` | Onboarding might be in progress even if the Google Cloud console shows the service as enabled. | Report an issue to the support team.  
`status.ErrInvalidArgument` | Field validation failures | Make sure that the `CreateConnector` request meets the specified constraints.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
