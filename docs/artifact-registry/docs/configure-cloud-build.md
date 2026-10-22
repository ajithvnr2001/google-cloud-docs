---
url: https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build/
title: Connect to Cloud Build \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:26.072414+00:00
---

# Connect to Cloud Build  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Connect to Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Cloud Build to store built artifacts in an Artifact Registry repository.

## Before you begin

  1. If the target repository does not exist in Artifact Registry, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. If Cloud Build and your repository are in different projects or if you are using a [user-specified service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) to run builds, [grant the Artifact Registry Writer role](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the build service account in the project with the repositories.

The default Cloud Build service account has access to perform the following actions with a repository in the same Google Cloud project:

     * Upload and download artifacts
     * Create [gcr.io repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories#gcr) in Artifact Registry



## Configure a Docker build

After you have granted permissions to the target repository, you are ready to configure your build.

To configure your build:

  1. In your build config file, add the step to build and tag the image.
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args: [ 'build', '-t', '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}', '.' ]
         images:
         - '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}'
         

This snippet uses Cloud Build substitutions. This approach is useful if you want to use the same build config file to push images to repositories for different environments, such as testing, staging, or production.

     * `${_LOCATION}`, `${_REPOSITORY}`, and `${_IMAGE}` are [user-defined substitution](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using-user-defined-substitutions) for the repository location, repository name, and image. You specify the values for these variables at build time.
     * `$PROJECT_ID` is a [default substitution](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using-default-substitutions) that Cloud Build resolves with the Google Cloud project ID for the build.

       * If you run the `gcloud builds submit` command, Cloud Build uses the active project ID in the gcloud session.
       * If you use a build trigger, Cloud Build uses the ID of the project where Cloud Build is running.

Alternatively, you can use a user-defined substitution instead of `$PROJECT_ID` so that you can specify a project ID at build time.

  2. When you are ready to run the build, specify values for the user-defined substitutions. For example, this command substitutes:

     * `us-east1` for the repository location
     * `my-repo` for the repository name
     * `my-image` for the image name
    
    gcloud builds submit --config=cloudbuild.yaml \
      --substitutions=_LOCATION="us-east1",_REPOSITORY="my-repo",_IMAGE="my-image" .
    




## Configure a Go build

After you have granted permissions to the target repository, you are ready to configure your build. The following instructions describe configuring your build to upload a Go module to a Go repository.

To configure your build:

  1. To upload a Go module to your Go repository in your build, add the following steps to your build config file:
         
         steps:
         - name: gcr.io/cloud-builders/gcloud
         args:
         - 'artifacts'
         - 'go'
         - 'upload'
         - '--project=$PROJECT_ID'
         - '--location=${_LOCATION}'
         - '--repository=${_REPOSITORY}'
         - '--module-path=${_MODULE_PATH}'
         - '--version=$TAG_NAME'
         

The build config file includes Cloud Build [substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using-user-defined-substitutions). This approach is useful if you want to use the same build config file to upload packages to repositories for different environments, such as testing, staging, or production.

     * `${_LOCATION}`, `${_REPOSITORY}`, and `${_MODULE_PATH}` are user-defined substitutions for the repository location, repository name, and module path. You specify the values for these variables at build time.
     * `$PROJECT_ID` and `$TAG_NAME` are [default substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using-default-substitutions) that Cloud Build replaces with the following:

       * `$PROJECT_ID` is replaced with the Google Cloud project ID for the build.

         * If you run the `gcloud builds submit` command, Cloud Build uses the active project ID in the gcloud session.
         * If you use a build trigger, Cloud Build uses the ID of the project where Cloud Build is running.

Alternatively, you can use a user-defined substitution instead of `$PROJECT_ID` so that you can specify a project ID at build time.

       * `$TAG_NAME` is replaced with the name of your tag to support the Go convention of using Git tags as version numbers.

  2. To install the package from the Go repository, add the following steps to your build config file to:

     * Add a regional Artifact Registry endpoint in your repository location to the `.netrc` file.
     * Run the credential helper tool to refresh OAuth tokens.
     * Run the `go run` command. You can also change this to `go build` to compile the module, `go test` to run tests, or `go mod tidy` to download the dependencies.

For the `go` command step, the `GOPROXY` is set to the Artifact Registry repository that hosts private dependencies. You can add the public proxy to the comma-separated `GOPROXY` list if the module has public dependencies.
    
    steps:
    - name: golang
      entrypoint: go
      args: ['run', 'github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.1.0', 'add-locations', '--locations=${_LOCATION}']
      env:
      # Set GOPROXY to the public proxy to pull the credential helper tool
      - 'GOPROXY=https://proxy.golang.org'
    - name: golang
      entrypoint: go
      args: ['run', 'github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.1.0', 'refresh']
      env:
      # Set GOPROXY to the public proxy to pull the credential helper tool
      - 'GOPROXY=https://proxy.golang.org'
    - name: golang
      entrypoint: go
      args: ['run', '.']
      env:
      - 'GOPROXY=https://${_LOCATION}-go.pkg.dev/${_PROJECT_ID}/${_REPOSITORY}'
    options:
      env:
      # Disable GO sumdb checks for private modules.
      - 'GONOSUMDB=${_MODULE_PATH}'
    

  3. When you are ready to run the build, specify values for the user-defined substitutions. For example, this command substitutes:

     * `us-east1` for the repository location
     * `my-project` for the project ID
     * `my-repo` for the repository name
     * `example.com/greetings` for the module path
    
    gcloud builds submit --config=cloudbuild.yaml \
      --substitutions=_LOCATION="us-east1",_PROJECT_ID="my-project",_REPOSITORY="my-repo",_MODULE_PATH="example.com/greetings" .
    




## Configure a Java build

After you have granted permissions to the target repository, you are ready to configure your build. The following instructions describe configuring your build to upload a Java package to a Maven repository.

To configure your build:

  1. Set up [authentication](https://docs.cloud.google.com/artifact-registry/docs/java/authentication#auth-helper) for Maven. Ensure that you specify the correct target project and repository in your `pom.xml` file.

  2. In your Cloud Build build config file, add the step to upload the package with Maven:
         
         steps:
         - name: gcr.io/cloud-builders/mvn
           args: ['deploy']
         

  3. When your build config file is ready, start your build with the following command:
         
         gcloud builds submit
         




## Configure a Node.js build

After you have granted permissions to the target repository, you are ready to configure your build. The following instructions describe configuring your build to upload a Node.js package to an npm repository.

To configure your build:

  1. Add your Artifact Registry repository to the `.npmrc` file in your Node.js project. The file is located in the directory with your `package.json` file.
         
         @SCOPE:registry=https://LOCATION-npm.pkg.dev/PROJECT_ID/REPOSITORY
         //LOCATION-npm.pkg.dev/PROJECT_ID/REPOSITORY/:always-auth=true
         

     * SCOPE-NAME is the name of the npm [scope](https://docs.cloud.google.com/artifact-registry/docs/nodejs#scopes) to associate with the repository. Using scopes ensures that you always publish and install packages from the correct repository.
     * PROJECT_ID is your Google Cloud project ID.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
     * REPOSITORY is the name of the repository.
  2. Add a script to the `package.json` file in your project that refreshes the access token for authentication with the repository.
         
         "scripts": {
          "artifactregistry-login": "npx google-artifactregistry-auth"
         }
         

  3. In your build config file, add the step to upload the package to the repository.
         
         steps:
         - name: gcr.io/cloud-builders/npm
           args: ['run', 'artifactregistry-login']
         - name: gcr.io/cloud-builders/npm
           args: ['publish', '${_PACKAGE}']
         

`${_PACKAGE}` is a Cloud Build [substitution](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using-user-defined-substitutions) that represents your Node.js project directory. You can specify the directory when you run the command to run the build.

For example, this command uploads the package from a directory named `src`:
         
         gcloud builds submit --config=cloudbuild.yaml \
             --substitutions=_PACKAGE="src" .
         




## Configure a Python build

After you have granted permissions to the target repository, you are ready to configure your build. The following instructions describe configuring your build to upload a Python package to a Python repository and install the package using pip.

To build and containerize a Python application and then push it to a Docker repository, see [Building Python applications](https://docs.cloud.google.com/build/docs/building/build-python) in the Cloud Build documentation.

To configure your build:

  1. In the directory with your Cloud Build build config file, create a file named `requirements.txt` with the following dependencies:
         
         twine
         keyrings.google-artifactregistry-auth
         

     * [Twine](https://twine.readthedocs.io/) is for uploading packages to Artifact Registry.
     * [keyrings.google-artifactregistry-auth](https://pypi.org/project/keyrings.google-artifactregistry-auth/) is the Artifact Registry key ring backend that handles authentication with Artifact Registry for pip and Twine.
  2. To upload a Python package to your Python repository in your build, add the following steps to your build config file:
         
         steps:
         - name: python
           entrypoint: pip
           args: ["install", "-r", "requirements.txt", "--user"]
         - name: python
           entrypoint: python
           args:
           - '-m'
           - 'twine'
           - 'upload'
           - '--repository-url'
           - 'https://${_LOCATION}-python.pkg.dev/$PROJECT_ID/${_REPOSITORY}/'
           - 'dist/*'
         

In this snippet, the first step installs Twine and the Artifact Registry key ring backend. The second step uploads your built Python files in the `dist` subdirectory. Adjust the paths to `requirements.txt` and your built Python files if they don't match the snippet.

The repository path includes Cloud Build [substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using-user-defined-substitutions). This approach is useful if you want to use the same build config file to upload packages to repositories for different environments, such as testing, staging, or production.

     * `${_LOCATION}` and `${_REPOSITORY}` are user-defined substitutions for the repository location, repository name, and package name. You specify the values for these variables at build time.
     * `$PROJECT_ID` is a [default substitution](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using-default-substitutions) that Cloud Build resolves with the Google Cloud project ID for the build.

       * If you run the `gcloud builds submit` command, Cloud Build uses the active project ID in the gcloud session.
       * If you use a build trigger, Cloud Build uses the ID of the project where Cloud Build is running.

Alternatively, you can use a user-defined substitution instead of `$PROJECT_ID` so that you can specify a project ID at build time.

  3. To install the package from the Python repository, add a step to your build config file that runs the `pip install` command.
         
         steps:
           - name: python
             entrypoint: pip
             args:
             - 'install'
             - '--index-url'
             - 'https://${_LOCATION}-python.pkg.dev/$PROJECT_ID/${_REPOSITORY}/simple/'
             - '${_PACKAGE}'
             - '--verbose'
         

This snippet includes an additional `${_PACKAGE}` substitution for the package name.

**Note:** Starting with pip 21.2, use the `--verbose` or `-v` flag up to three times for additional debugging output. For example to get the next level of debugging detail, use `--verbose --verbose` or `-vv`.
  4. When you are ready to run the build, specify values for the user-defined substitutions. For example, this command substitutes:

     * `us-east1` for the repository location
     * `my-repo` for the repository name
     * `my-package` for the package name
    
    gcloud builds submit --config=cloudbuild.yaml \
      --substitutions=_LOCATION="us-east1",_REPOSITORY="my-repo",_PACKAGE="my-package" .
    




## Store artifacts in a private registry using self-signed certificates

If you have a private certificate authority and need to store artifacts in a private registry, then you can set up your build config file to use self-signed certificates. To do so, add a build step that pushes your certificate to the host system so that the certificate is available for subsequent build steps. For example:
    
    
    - name: gcr.io/cloud-builders/docker
      args:
        - run
        - --rm
        - --volume=/etc/docker/certs.d/:/etc/docker/certs.d/
        - --volume=certificates:/certificates
        - ubuntu
        - bash
        - -c
        - |
          cp /certificates/ca.crt /etc/docker/certs.d/quay.apps.cloud.inter
      volumes:
        - name: certificates
          path: /certificates
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
