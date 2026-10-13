---
url: https://docs.cloud.google.com/artifact-registry/docs/reference/docker-api/
title: Support for the Docker Registry API \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:00.783721+00:00
---

# Support for the Docker Registry API  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/reference/docker-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-registry/docs/apis)



Send feedback 

#  Support for the Docker Registry API Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry implements version 1.1 of the Open Container Initiative (OCI) Distribution Specification so that you can push and pull images directly with Docker clients, including the [Docker command-line tool](https://docs.docker.com/engine/reference/commandline/cli/).

Google Cloud services that typically integrate with Artifact Registry, such as Cloud Build and Google Kubernetes Engine, are configured by with [default permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#integration) to access repositories in the same project and don't require a separate client.

If you want to interact with Artifact Registry without the Docker client, then we recommend using the [gcrane](https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md) tool. The tool provides:

  * Standard commands that work with Artifact Registry and other registries.
  * Commands for Artifact Registry tasks that don't have an equivalent command in the Google Cloud CLI or the Docker command-line tool, such as listing untagged images or copying images across registry hosts.



If gcrane isn't an appropriate option, then you can use the OCI Distribution Specification:

  * Refer to the [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec/blob/main/spec.md) for information about the OCI request format.
  * See Authenticating using the Docker Registry API for information about authentication using the API.

**Note:** Artifact Registry doesn't support Docker [chunked uploads](https://docs.docker.com/registry/spec/api/#chunked-upload). Some container image tools support uploading large container images with either chunked uploads or a single [monolithic upload](https://docs.docker.com/registry/spec/api/#monolithic-upload). You must use monolithic uploads when you push container images to Artifact Registry.

## Make requests to Artifact Registry using the OCI Distribution Specification

If using Docker or the `gcrane` tool isn't an option, then you can use the OCI Distribution Specification.

First, grant the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to your user account. You can then use the Google Cloud CLI to create an access token for requests.

The following example shows the command for [listing tags](https://docs.docker.com/registry/spec/api/#listing-image-tags), using `my-image` as the image and `my-project` as the Google Cloud project. This example also uses the [jq](https://stedolan.github.io/jq/) command to filter and format the output returned by requests, but it's optional. The `jq` tool is included in Cloud Shell.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://us-docker.pkg.dev/v2/my-project/my-repo/my-image/tags/list" | jq ".tags"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
