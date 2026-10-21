---
url: https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance/
title: Generate and validate build provenance \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:09.296646+00:00
---

# Generate and validate build provenance  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Generate and validate build provenance Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to generate build provenance, view the output, and validate it.

Build provenance is a collection of verifiable data about a build. Provenance metadata includes details such as the digests of the built images, the input source locations, the build arguments, and the build duration. You can use this information to ensure that the built artifacts you are using are accurate and reliable, created by trusted sources and builders.

Cloud Build supports the generation of build provenance that meets Supply-chain Levels for Software Artifacts (SLSA) level 3 assurance based on the specifications for SLSA version [0.1](https://slsa.dev/spec/v0.1/) and [1.0](https://slsa.dev/spec/v1.0/).

As part of support for the SLSA v1.0 spec, Cloud Build provides **`buildType`** details in build provenance. You can use the `buildType` schema to understand the parameterized template used for the build process, including the values that Cloud Build records, and the source of those values. For more information, see [Cloud Build buildType v1](https://docs.cloud.google.com/build/gcb-buildtypes/google-worker/v1).

## Limitations

  * Cloud Build only generates build provenance for artifacts stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).
  * Repository [attachments](https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments), including build provenance, aren't subject to [cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy-overview). Instead, attachments are deleted when the image they are attached to is deleted. For more information, see [Manage attachments with cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments#attach-cleanup).



## Before you begin

  1. Enable the Cloud Build, Container Analysis, and Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,containeranalysis.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/generate-verifiable-provenance%7B%7Bdynamic_data.request.path%7D%7D)

  2. To use the command-line examples in this guide, install and configure the [Google Cloud SDK](https://docs.cloud.google.com/sdk).

**Note:** If you've installed Google Cloud SDK previously, make sure you have the latest available version by running `gcloud components update`.
  3. Have your source code handy.

  4. Have a [repository in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).




## Generate build provenance

The following instructions explain how to generate build provenance for container images you store in Artifact Registry:

  1. In your build config file, add the `images` field to configure Cloud Build to store your built images in Artifact Registry after your build completes.

Cloud Build can't generate provenance if you push your image to Artifact Registry using an explicit `docker push` step.

The following snippet shows a build config to build a container image and store the image in a Docker repository in Artifact Registry:

###  YAML 
         
         steps:
           - name: 'gcr.io/cloud-builders/docker'
             args: [ 'build', '-t', 'LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE', '.' ]
           images: ['LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE']
         

Where:

     * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for your repository.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REPOSITORY`: the name of your Artifact Registry repository.
     * `IMAGE`: the name of your your container image.

###  JSON 
    
    {
      "steps": [
          {
              "name": "gcr.io/cloud-builders/docker",
              "args": [
                  "build",
                  "-t",
                  "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE",
                  "."
              ]
          }
      ],
      "images": [
          "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE"
      ]
      }
    

Where:

     * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for your repository.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REPOSITORY`: the name of your Artifact Registry repository.
     * `IMAGE`: the name of your your container image.

  2. In the `options` section of your build config, add the `requestedVerifyOption` option and set to the value `VERIFIED`.

This setting enables provenance generation and configures Cloud Build to verify that provenance metadata is present. Builds will only be marked successful if provenance is generated.

###  YAML 
         
         options:
           requestedVerifyOption: VERIFIED
         

###  JSON 
         
         {
             "options": {
                 "requestedVerifyOption": "VERIFIED"
             }
         }
         

  3. Start your build.




## View build provenance

This section explains how to view the build provenance metadata created by Cloud Build. You can fetch this information for auditing purposes.

You can access build provenance metadata for containers by using the **Security insights** side panel within the Google Cloud console, or by using the gcloud CLI.

###  console 

The **Security insights** side panel provides a high-level overview of security information for artifacts stored in Artifact Registry.

To view the **Security insights** panel:

  1. Open the **Build History** page in the Google Cloud console:

[Open the Build History page](https://console.cloud.google.com/cloud-build/builds)

  2. In the table with the builds, locate the row with the build for which you want to view security insights.

  3. Under the **Security insights** column, click **View**.

This displays the **Security insights** panel for the selected artifact.

The **Build** card displays provenance details and a link. You can view the provenance snippet by clicking on the link icon.




To learn more about the side panel and how you can use Cloud Build to help protect your software supply chain, see [View build security insights](https://docs.cloud.google.com/build/docs/view-build-security-insights).

###  gcloud CLI 

To view provenance metadata for container images, run the following command:
    
    
      gcloud artifacts docker images describe \
      LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE@sha256:HASH \
      --show-provenance --format=FORMAT
    

Replace the following:

  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for your repository.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REPOSITORY`: the name of your Artifact Registry repository.
  * `IMAGE`: the name of your your container image.
  * `HASH`: The sha256 hash value of the image. You can find this in the output of your build.
  * `FORMAT`: An optional setting where you can specify an output [format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats).



### Example output

The build provenance resembles the following:
    
    
          image_summary:
          digest: sha256:7e9b6e7ba2842c91cf49f3e214d04a7a496f8214356f41d81a6e6dcad11f11e3
          fully_qualified_digest: us-central1-docker.pkg.dev/my-project/my-repo/my-image@sha256:7e9b6e7ba2842c91cf49f3e214d04a7a496f8214356f41d81a6e6dcad11f11e3
          registry: us-central1-docker.pkg.dev
          repository: my-repo
          slsa_build_level: 0
        provenance_summary:
          provenance:
          - build:
              inTotoSlsaProvenanceV1:
                _type: https://in-toto.io/Statement/v1
                predicate:
                  buildDefinition:
                    buildType: https://cloud.google.com/build/gcb-buildtypes/google-worker/v1
                    externalParameters:
                      buildConfigSource:
                        path: cloudbuild.yaml
                        ref: refs/heads/main
                        repository: git+https://github.com/my-username/my-git-repo
                      substitutions: {}
                    internalParameters:
                      systemSubstitutions:
                        BRANCH_NAME: main
                        BUILD_ID: e73ca1d4-ec4a-4ea6-acdd-ac8bb16dcc79
                        COMMIT_SHA: 525c52c501739e6df0609ed1f944c1bfd83224e7
                        LOCATION: us-west1
                        PROJECT_NUMBER: '265426041527'
                        REF_NAME: main
                        REPO_FULL_NAME: my-username/my-git-repo
                        REPO_NAME: my-git-repo
                        REVISION_ID: 525c52c501739e6df0609ed1f944c1bfd83224e7
                        SHORT_SHA: 525c52c
                        TRIGGER_BUILD_CONFIG_PATH: cloudbuild.yaml
                        TRIGGER_NAME: github-trigger-staging
                      triggerUri: projects/265426041527/locations/us-west1/triggers/a0d239a4-635e-4bd3-982b-d8b72d0b4bab
                    resolvedDependencies:
                    - digest:
                        gitCommit: 525c52c501739e6df0609ed1f944c1bfd83224e7
                      uri: git+https://github.com/my-username/my-git-repo@refs/heads/main
                    - digest:
                        sha256: 154fcd4d2d65c6a35b06b98053a0829c581e223d530be5719326f5d85d680e8d
                      uri: gcr.io/cloud-builders/docker@sha256:154fcd4d2d65c6a35b06b98053a0829c581e223d530be5719326f5d85d680e8d
                  runDetails:
                    builder:
                      id: https://cloudbuild.googleapis.com/GoogleHostedWorker
                    byproducts:
                    - {}
                    metadata:
                      finishedOn: '2023-08-01T19:57:10.734471Z'
                      invocationId: https://cloudbuild.googleapis.com/v1/projects/my-project/locations/us-west1/builds/e73ca1d4-ec4a-4ea6-acdd-ac8bb16dcc79
                      startedOn: '2023-08-01T19:56:57.451553160Z'
                predicateType: https://slsa.dev/provenance/v1
                subject:
                - digest:
                    sha256: 7e9b6e7ba2842c91cf49f3e214d04a7a496f8214356f41d81a6e6dcad11f11e3
                  name: https://us-central1-docker.pkg.dev/my-project/my-repo/my-image
                - digest:
                    sha256: 7e9b6e7ba2842c91cf49f3e214d04a7a496f8214356f41d81a6e6dcad11f11e3
                  name: https://us-central1-docker.pkg.dev/my-project/my-repo/my-image:latest
            createTime: '2023-08-01T19:57:14.810489Z'
            envelope:
              payload:
              eyJfdHlwZSI6Imh0dHBzOi8vaW4tdG90by5pby9TdGF0ZW1lbnQvdMWQ0LWVjNGEtNGVhNi1hY2RkLWFjOGJiMTZkY2M3OSIsICJzdGFydGVkT24iOiIyMDIzLTA4LTAxVDE5OjU2OjU3LjQ1MTU1MzE2MFoiLCAiZmluaXNoZWRPbiI6IjIwMjMtMDgtMDFUMTk6NTc6MTAuNzM0NDcxWiJ9LCAiYnlwcm9kdWN0cyI6W3t9XX19fQ==...
              payloadType: application/vnd.in-toto+json
              signatures:
              - keyid: projects/verified-builder/locations/global/keyRings/attestor/cryptoKeys/google-hosted-worker/cryptoKeyVersions/1
                sig: MEUCIQCss8UlQL2feFePRJuKTE8VA73f85iqj4OJ9SvVPqTNwAIgYyuyuIrl1PxQC5B109thO24Y6NA4bTa0PJY34EHRSVE=
            kind: BUILD
            name: projects/my-project/occurrences/71787589-c6a6-4d6a-a030-9fd041e40468
            noteName: projects/argo-qa/notes/intoto_slsa_v1_e73ca1d4-ec4a-4ea6-acdd-ac8bb16dcc79
            resourceUri: https://us-central1-docker.pkg.dev/my-project/my-repo/my-image@sha256:7e9b6e7ba2842c91cf49f3e214d04a7a496f8214356f41d81a6e6dcad11f11e3
            updateTime: '2023-08-01T19:57:14.810489Z'
        

A few important things to notice in this example:

  * **Source** : The [build was triggered from a GitHub repository](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github).

  * **Object reference** : Fields named `digest` and `fileHash` refer to the same object. The `digest` field included in the example output is encoded in base 16 (hex-encoded). If you're using SLSA version 0.1 provenance, your output uses the `fileHash` field encoded in base 64.

  * **Signatures** : If you're using SLSA version 0.1 provenance, your output contains two signatures on the `envelope` field. The first signature, which has the key name `provenanceSigner`, uses a [DSSE-conformant signature](https://github.com/secure-systems-lab/dsse/blob/master/protocol.md) (formatted with [Pre-Authentication Encoding (PAE)](https://github.com/secure-systems-lab/dsse/blob/master/protocol.md#signature-definition)), which can be verified in [Binary Authorization](https://docs.cloud.google.com/binary-authorization) policies. We recommend that you use this signature in new usages of this provenance. The second signature, which has the key name `builtByGCB`, is provided for legacy usage.

  * **Service accounts** : The signatures that are automatically included in Cloud Build provenance help you verify the build service that executed a build. You can also configure Cloud Build to record verifiable metadata about the service account used to initiate a build. For more information, see [sign container images with cosign](https://docs.cloud.google.com/build/docs/building/build-containers#use-cosign).

  * **Payload** : The example provenance displayed on this page is shortened for readability. Actual output will be longer, as the payload is a base-64 encoded version of the all of the provenance metadata.

  * **Dependencies** : [Dependencies you specify](https://docs.cloud.google.com/build/docs/building/manage-dependencies) in your build file are included in provenance, in the `resolvedDependencies` field.




## View provenance for non-container artifacts

Cloud Build generates [SLSA](https://slsa.dev/) provenance metadata for standalone Go, Java (Maven), Python, and Node.js (npm) applications when you upload your build artifacts to Artifact Registry.

  1. To generate the provenance metadata for your artifacts, run a build with Cloud Build. Use one of the following guides:

     * [Build standalone Go applications](https://docs.cloud.google.com/build/docs/building/build-go)
     * [Build standalone Java applications](https://docs.cloud.google.com/build/docs/building/build-java)
     * [Build standalone Python applications](https://docs.cloud.google.com/build/docs/building/build-python)
     * [Build standalone Node.js applications](https://docs.cloud.google.com/build/docs/building/build-nodejs)

When your build completes, note the `BuildID`.

  2. You can retrieve the provenance metadata by making a direct API call or using the `gcloud` CLI. To find the provenance for a specific build, you should filter the results by the Build ID.

###  gcloud 
         
         gcloud container analysis occurrences list \
           --project="PROJECT_ID" \
           --filter='kind="BUILD" AND build.inTotoSlsaProvenanceV1.predicate.runDetails.metadata.invocationId="https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/builds/BUILD_ID"' \
           --format=json
         

###  curl 
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         
         PROJECT_ID="PROJECT_ID"
         LOCATION="LOCATION"
         BUILD_ID="BUILD_ID"
         
         FILTER="kind%3D%22BUILD%22%20AND%20build.inTotoSlsaProvenanceV1.predicate.runDetails.metadata.invocationId%3D%22https%3A%2F%2Fcloudbuild.googleapis.com%2Fv1%2Fprojects%2F${PROJECT_ID}%2Flocations%2F${LOCATION}%2Fbuilds%2F${BUILD_ID}%22"
         
         gcurl "https://containeranalysis.googleapis.com/v1/projects/${PROJECT_ID}/occurrences?filter=${FILTER}"
         

Replace the placeholders in the preceding examples:

     * `PROJECT_ID`: Your Google Cloud project ID.
     * `LOCATION`: The region where the build was executed such as, `us-central1`.
     * `BUILD_ID`: The ID of the build you are interested in.

This returns the specific `BUILD` kind occurrence(s) matching the specified Build ID.

_Note:_ Filtering on nested JSON fields like `invocationId` might be slower than filtering on top-level indexed fields, especially in projects with a very large number of occurrences.




## Validate provenance

This section explains how to validate build provenance for container images.

Validating build provenance helps you to:

  * confirm that build artifacts are being generated from trusted sources and builders
  * ensure that provenance metadata describing your build process is complete and authentic



For more information, see [Safeguard builds](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds#provenance).

### Validate provenance using the SLSA verifier

The [SLSA verifier](https://github.com/slsa-framework/slsa-verifier) is an open source CLI tool for validating build integrity based on the SLSA specifications.

If the verifier finds issues, it returns detailed error messages to help you update your build process and mitigate risks.

To use the SLSA verifier, do the following:

  1. Install version 2.1 or higher from the [slsa-verifier repository](https://github.com/slsa-framework/slsa-verifier#installation)
         
         go install github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier@VERSION
         

  2. In your CLI, set a variable for your image identifier:
         
         export IMAGE=LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE@sha256:HASH
         

Where:

     * `LOCATION`: Regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations).
     * `PROJECT_ID`: Google Cloud project ID.
     * `REPOSITORY`: Name of the repository.
     * `IMAGE`: Image name.
     * `HASH`: The sha256 hash value of the image. You can find this in the output of your build.
  3. Authorize the gcloud CLI so that the SLSA verifier can access your provenance data:
         
         gcloud auth configure-docker LOCATION-docker.pkg.dev
         

  4. Retrieve the provenance for your image and store it as `JSON`:
         
         gcloud artifacts docker images describe $IMAGE --format json --show-provenance > provenance.json
         

  5. Verify the provenance:
         
         slsa-verifier verify-image "$IMAGE" \
         --provenance-path provenance.json \
         --source-uri SOURCE \
         --builder-id=BUILDER_ID
         

Where:

     * `SOURCE` is the source repository URI for your image, for example `github.com/my-repo/my-application`.
     * `BUILDER_ID` the unique ID for the builder, for example `https://cloudbuild.googleapis.com/GoogleHostedWorker`

If you want to print the validated provenance for use in a policy engine, use the previous command with the `--print-provenance` flag.

The output is similar to the following: `PASSED: Verified SLSA provenance` or `FAILED: SLSA verification failed: <error details>`.




For more information on optional flags, see [options](https://github.com/slsa-framework/slsa-verifier#option-list).

### Validate provenance metadata with the gcloud CLI

If you want to verify that the build provenance metadata has not been tampered with, you can validate the provenance by performing the following steps:

  1. Create a new directory and go to that directory.
         
         mkdir provenance && cd provenance
         

  2. Using the information from the `keyid` field, get the public key.
         
         gcloud kms keys versions get-public-key 1 --location global --keyring attestor \
           --key builtByGCB --project verified-builder --output-file my-key.pub
         

  3. The `payload` contains the JSON representation of the provenance, encoded in base64url. Decode the data and store it in a file.
         
         gcloud artifacts docker images describe \
         LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE@sha256:HASH --show-provenance \
           --format=json | jq -r '.provenance_summary.provenance[] | select(.build.intotoStatement.predicateType == "https://slsa.dev/provenance/v0.1") | .envelope.payload' | tr '\-_' '+/' | base64 -d > provenance.json
         

Both SLSA version 0.1 and 1.0 provenance types are stored when available. If you want to filter for version 1.0, change the `predicateType` to use `https://slsa.dev/provenance/v1`. For example:
         
         gcloud artifacts docker images describe \
         LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE@sha256:HASH --show-provenance \
           --format=json | jq -r '.provenance_summary.provenance[] | select(.build.intotoStatement.predicateType == "https://slsa.dev/provenance/v1") | .envelope.payload' | tr '\-_' '+/' | base64 -d > provenance.json
         

  4. The envelope also contains the signature over the provenance. Decode the data and store it in a file.
         
         gcloud artifacts docker images describe LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE@sha256:HASH --show-provenance \
           --format=json | jq -r '.provenance_summary.provenance[] | select(.build.intotoStatement.predicateType == "https://slsa.dev/provenance/v0.1") | .envelope.signatures[0].sig' | tr '\-_' '+/' | base64 -d > signature.bin
         

If you want to filter for version 1.0, change the `predicateType` to use `https://slsa.dev/provenance/v1`. For example:
         
         gcloud artifacts docker images describe LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE@sha256:HASH --show-provenance \
         --format=json | jq -r '.provenance_summary.provenance[] | select(.build.intotoStatement.predicateType == "https://slsa.dev/provenance/v1") | .envelope.signatures[0].sig' | tr '\-_' '+/' | base64 -d > signature.bin
         

  5. The command above references the first provenance signature (`.provenance_summary.provenance[0].envelope.signatures[0]`) which is signed by the `provenanceSigner` key. The payload is signed over the [PAE-formatted envelope](https://github.com/secure-systems-lab/dsse/blob/master/protocol.md#signature-definition). In order to verify it, run this command to transform the provenance into the expected PAE format of `"DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(body) + SP + body`.

**Note:** If you are verifying the second signature (`.provenance_summary.provenance[0].envelope.signatures[1].sig` with keyname `builtByGCB`), skip this step and verify the provenance.json file you have already stored.
         
         echo -n "DSSEv1 28 application/vnd.in-toto+json $(cat provenance.json | wc -c) $(cat provenance.json)" > provenance.json
         

  6. Validate the signature.
         
         openssl dgst -sha256 -verify my-key.pub -signature signature.bin provenance.json
         

After a successful validation, the output is `Verified OK`.




## What's next

  * [Configure Cloud Build to track who initiates a build](https://docs.cloud.google.com/build/docs/building/build-containers#use-cosign)
  * [Use vulnerability scanning in your Cloud Build pipeline](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis)
  * [Learn about software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
