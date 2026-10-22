---
url: https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection/
title: Validate your connection \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:50.818365+00:00
---

# Validate your connection  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Validate your connection Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you confirm that your service accounts and AWS accounts are successfully enabled for accessing the Assured Open Source Software service.

To validate whether your Google Cloud service accounts or (for the free tier only) AWS account ID is enabled for access to the Assured OSS repository and portfolio of curated packages, list the available Java, Python, Go, or JavaScript (NPM) packages using an API. To do this, you can either directly call the APIs, or use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell) to run a curl command line call to the API.

If you're using the free tier, in rare cases, you might face permission denied errors for an hour or more after you submit the [customer enablement form](https://developers.google.com/assured-oss#get-started) submission.

This document applies to both the premium tier and free tier.

## Before you begin

  1. Install the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). If you installed Google Cloud CLI previously, make sure you have the latest version by running the following:
         
         gcloud components update
         

  2. To access Assured OSS using Google Cloud, [enable the Artifact Registry API](https://docs.cloud.google.com/artifact-registry/docs/enable-service) for the parent Google Cloud project of the service accounts that you enabled for Assured OSS. If you are using the premium tier, the API is enabled during setup.

  3. Add the following URLs to your network's allowlist:

     * `*.pkg.dev`
     * `artifactregistry.googleapis.com`



## Set up authentication

### For Google Cloud

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  1. Generate and download the [service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating). We recommend following the [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

  2. If you are already logged in to Google Cloud CLI, revoke any existing authentication:
         
         gcloud auth revoke
         

  3. Authenticate to Google Cloud:
         
         gcloud auth login --cred-file=FILEPATH.json
         

Where FILEPATH is the path to the service account key.

  4. Update the [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials):
         
         export GOOGLE_APPLICATION_CREDENTIALS=FILEPATH.json
         

Where FILEPATH is the path to the service account key.




### For AWS

These steps apply to the free tier of Assured OSS only.

  1. [Set up your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) to allow requesting [temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html).

     1. Sign in to the [AWS Management Console](https://aws.amazon.com/).
     2. In the AWS Management Console, go to the EC2 dashboard and select your target EC2 instance.
     3. Select **Actions > Security > Modify IAM Role**.
     4. Select **Create New IAM Role > Create role**.
     5. For the trusted entity type, select **AWS Service**.
     6. For the use case, choose **EC2**.
     7. Add the **AmazonEC2ReadOnlyAccess** permission and click **Next**.
     8. Provide a meaningful name for the IAM role and click **Next**.
     9. Go back to **Modify IAM Role**. Select the newly created role and click **Update IAM Role**.
  2. Generate the credential configuration file:
         
         gcloud iam workload-identity-pools create-cred-config \
         projects/ASSIGNED_PROJECT_NUMBER/locations/global/workloadIdentityPools/aoss-wif-pool/providers/aws-AWS_ACCOUNT_ID-provider \
         --service-account=aoss-wif-aws-AWS_ACCOUNT_ID-sa@ASSIGNED_PROJECT_ID.iam.gserviceaccount.com \
         --aws \
         --output-file=FILEPATH.json
         

Replace the following:

     * AWS_ACCOUNT_ID: The 12-digit number for your AWS account (for example, `123456789012`).
     * FILEPATH: The file to save configuration to. + ASSIGNED_PROJECT_ID: The Google Cloud project ID assigned to you, as mentioned in your enablement mail. + ASSIGNED_PROJECT_NUMBER: The Google Cloud project number assigned to you, as mentioned in your enablement mail.

If you use [AWS IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html), add the flag `--enable-imdsv2` to the preceding command. For more information, see [Create a credential configuration](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#create_a_credential_configuration).

  3. If you are already logged in to Google Cloud CLI, revoke any existing authentication:
         
         gcloud auth revoke
         

  4. Authenticate to Google Cloud:
         
         gcloud auth login --cred-file=FILEPATH.json
         

Where FILEPATH is the path to the credential config file.

  5. Update [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials):
         
         export GOOGLE_APPLICATION_CREDENTIALS=FILEPATH.json
         

Where FILEPATH is the path to the service account key or the credential config file.




For troubleshooting issues related to authentication, see [Troubleshooting authentication errors](https://docs.cloud.google.com/assured-open-source-software/docs/troubleshooting#authentication-errors).

## List all Java packages available in Assured OSS

You can use a [REST API](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts/list) to list all the Java packages and their versions.

For the free tier of Assured OSS, enter the following HTTP request:
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts"
    

For the premium tier of Assured OSS, enter the following HTTP request:
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-java/packages
    

Replace PROJECT_ID with the ID of the project that you selected when you set up Assured OSS.

The following is a sample curl command to connect to the Java repository on the free tier:
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts"
    

The request returns a response similar to the following sample response:
    
    
      {
        "mavenArtifacts": [
          {
            "name":
      "projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts/com.alibaba:fastjson:1.2.83",
            "pomUri":
      "us-maven.pkg.dev/cloud-aoss/cloud-aoss-java/com/alibaba/fastjson/1.2.83/fastjson-1.2.83.pom",
            "groupId": "com.alibaba",
            "artifactId": "fastjson",
            "version": "1.2.83",
            "createTime": "2022-06-24T09:10:05.166879Z",
            "updateTime": "2022-06-24T09:10:05.166879Z"
          },
          {
            "name":
      "projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts/org.apache.logging.log4j:log4j-api:2.17.1",
            "pomUri":
      "us-maven.pkg.dev/cloud-aoss/cloud-aoss-java/org/apache/logging/log4j/log4j-api/2.17.1/log4j-api-2.17.1.pom",
            "groupId": "org.apache.logging.log4j",
            "artifactId": "log4j-api",
            "version": "2.17.1",
            "createTime": "2022-03-16T12:22:50.113695Z",
            "updateTime": "2022-03-16T12:22:50.113695Z"
          },
          {
            "name":
      "projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts/org.apache.logging.log4j:log4j-core:2.17.1",
          "pomUri":
      "us-maven.pkg.dev/cloud-aoss/cloud-aoss-java/org/apache/logging/log4j/log4j-core/2.17.1/log4j-core-2.17.1.pom",
            "groupId": "org.apache.logging.log4j",
            "artifactId": "log4j-core",
            "version": "2.17.1",
            "createTime": "2022-03-16T12:26:40.317215Z",
            "updateTime": "2022-03-16T12:26:40.317215Z"
          }
        ]
      }
    

If there are many available packages, the API response may be paginated. When the listing is incomplete, the continuation token `nextPageToken` is returned in the response. The `nextPageToken` represents the last result that is returned. When you pass the value of `nextPageToken` to the pageToken parameter of a subsequent request, you return the next page of results, starting after the last result.

To view the next page of results, or increase the number of objects returned per page, use the following URL:
    
    
      "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts?pageSize=NUMBER&pageToken=NEXT_PAGE_TOKEN"
    

Replace the following:

  * NUMBER: The number of items to be returned per page. The maximum accepted value is 1000.
  * NEXT_PAGE_TOKEN: The `nextPageToken` token value returned in the JSON response.



Alternatively, you can use the following script to collect the paginated results of the aforementioned API request into a file:
    
    
    tempFile=$(mktemp)
    nextPageToken=""
    while
        curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts?pageSize=1000&pageToken=$nextPageToken" > $tempFile
        nextPageToken=$(grep nextPageToken $tempFile | sed 's/  "nextPageToken": "//' | sed 's/.$//')
        grep -v nextPageToken $tempFile >> FILENAME1
        [ -n "$nextPageToken" ]
    do
    :
    done
    

### Optional: Write sorted list of primary Java package names to `FILENAME2`

The following additional command line actions filter the returned raw list of Java packages to give you a list of just the primary package names.
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts?pageSize=1000" \
          | grep artifactId | sort -f | uniq >  FILENAME2
    

### Optional: Write sorted list of the Java package versions to `FILENAME3`

The following additional command line actions filter the returned raw list of Java packages to give you a list of just the package versions.
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-java/mavenArtifacts?pageSize=1000" \
          | grep name | sort -f | uniq >  FILENAME3
    

## List all Python packages available in Assured OSS

You can use a [REST API](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.pythonPackages/list) to list all the Python packages and their versions. These packages are available for Python 3.8.

For the free tier of Assured OSS, enter the following HTTP request:
    
    
      GET https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages
    

For the premium tier of Assured OSS, enter the following HTTP request:
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        "https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-python/packages"
    

Replace PROJECT_ID with the ID of the project that you selected when you set up Assured OSS.

To list all packages specific to your environment, [use the `generator.sh` script](https://docs.cloud.google.com/assured-open-source-software/docs/pythonaccess#option_1_use_a_script_to_generate_a_single_requirements_file_for_all_artifacts).

The following command is a sample curl command to connect to the Assured OSS Python repository on the free tier:
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages"
    

The request returns a response similar to the following sample response:
    
    
      {
      "pythonPackages": [
        {
          "name":
      "projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages/Flask:2.1.2",
          "uri":
      "us-python.pkg.dev/cloud-aoss/cloud-aoss-python/flask/Flask-2.1.2-py3-none-any.whl",
            "packageName": "Flask",
            "version": "2.1.2",
            "createTime": "2022-07-13T11:06:54.163313Z",
            "updateTime": "2022-07-13T11:06:54.163313Z"
        },
        {
          "name":
      "projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages/ujson:5.3.0",
            "uri":
      "us-python.pkg.dev/cloud-aoss/cloud-aoss-python/ujson/ujson-5.3.0-cp38-cp38-linux_x86_64.whl",
            "packageName": "ujson",
            "version": "5.3.0",
            "createTime": "2022-07-13T11:06:17.263638Z",
            "updateTime": "2022-07-13T11:06:17.263638Z"
          },
          {
            "name":
      "projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages/ujson:5.4.0",
            "uri":
      "us-python.pkg.dev/cloud-aoss/cloud-aoss-python/ujson/ujson-5.4.0-cp38-cp38-linux_x86_64.whl",
            "packageName": "ujson",
            "version": "5.4.0",
            "createTime": "2022-07-13T11:09:00.865162Z",
            "updateTime": "2022-07-13T11:09:00.865162Z"
          },
          {
            "name":
      "projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages/urllib3:1.26.8",
            "uri":
      "us-python.pkg.dev/cloud-aoss/cloud-aoss-python/urllib3/urllib3-1.26.8-py2.py3-none-any.whl",
            "packageName": "urllib3",
            "version": "1.26.8",
            "createTime": "2022-07-13T11:05:56.529484Z",
            "updateTime": "2022-07-13T11:05:56.529484Z"
          }
        ]
      }
    

If there are many available packages, the API response may be paginated. When the listing is incomplete, the continuation token `nextPageToken` is returned in the response. The `nextPageToken` represents the last result that's returned. When you pass the value of `nextPageToken` to the pageToken parameter of a subsequent request, you return the next page of results, starting after the last result.

To view the next page of results, or increase the number of objects returned per page, use the following URL in the free tier:
    
    
      "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages?pageSize=NUMBER&pageToken=NEXT_PAGE_TOKEN"
    

Replace the following:

  * NUMBER: The number of items to be returned per page. The maximum accepted value is 1000.
  * NEXT_PAGE_TOKEN: The `nextPageToken` token value returned in the JSON response.



Alternatively, you can use the following script to collect the paginated results of the aforementioned API request into a file.
    
    
    tempFile=$(mktemp)
    nextPageToken=""
    while
        curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages?pageSize=1000&pageToken=$nextPageToken" > $tempFile
        nextPageToken=$(grep nextPageToken $tempFile | sed 's/  "nextPageToken": "//' | sed 's/.$//')
        grep -v nextPageToken $tempFile >> FILENAME4
        [ -n "$nextPageToken" ]
    do
    :
    done
    

### Optional: Write sorted list of primary Python package names to `FILENAME5`

The following additional command line actions filter the returned raw list of Python packages to give you a list of only the primary package names.
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages?pageSize=1000" \
          | grep packageName | sort -f | uniq > FILENAME5
    

### Optional: write sorted list of the Python package versions to `FILENAME6`

The following additional command line actions filter the returned raw list of Python packages to give you a list of just the package versions.
    
    
      curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/cloud-aoss-python/pythonPackages?pageSize=1000" \
          | grep name | sort -f | uniq >  FILENAME6
    

## List all Go packages available in Assured OSS

You can use a REST API to list all the Go packages and their versions.

For the free tier of Assured OSS, enter the following HTTP request:
    
    
    curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages"
    

For the premium tier of Assured OSS, enter the following HTTP request:
    
    
    curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-go/packages
    

Replace PROJECT_ID with the ID of the project that you selected when you set up Assured OSS.

The following is a sample curl command to connect to the Go repository on the free tier:
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \ https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages
    

The request returns a response similar to the following:
    
    
    {
      "packages": [
        {
          "name": "projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages/cloud.google.com%2Fgo%2Fauth",
          "createTime": "2025-08-05T06:04:54.442071Z",
          "updateTime": "2025-08-05T06:04:54.442071Z"
        },
        {
          "name": "projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages/cloud.google.com%2Fgo%2Fauth%2Foauth2adapt",
          "createTime": "2025-08-05T06:04:41.242052Z",
          "updateTime": "2025-08-05T06:04:41.242052Z"
        },
        {
          "name": "projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages/cloud.google.com%2Fgo%2Fcompute%2Fmetadata",
          "createTime": "2025-08-05T06:05:31.140186Z",
          "updateTime": "2025-08-05T06:05:31.140186Z"
        },
        {
          "name": "projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages/cloud.google.com%2Fgo%2Fiam",
          "createTime": "2025-08-05T06:04:54.455300Z",
          "updateTime": "2025-08-05T06:04:54.455300Z"
        },
        {
          "name": "projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages/cloud.google.com%2Fgo%2Flogging",
          "createTime": "2025-08-05T06:05:36.186851Z",
          "updateTime": "2025-08-05T06:05:36.186851Z"
        }
      ]
    }
    

If many packages are available, the API response might be paginated. When the listing is incomplete, the continuation token `nextPageToken` is returned in the response. The `nextPageToken` represents the last result that's returned. When you pass the value of `nextPageToken` to the `pageToken` parameter of a subsequent request, you return the next page of results, starting after the last result.

To view the next page of results or increase the number of objects returned per page, use the following URL:
    
    
    "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages?pageSize=NUMBER&pageToken=NEXT_PAGE_TOKEN"
    

Replace the following:

  * NUMBER: The number of items to be returned per page. The maximum accepted value is 1000.
  * NEXT_PAGE_TOKEN: The `nextPageToken` token value returned in the JSON response.



Alternatively, you can use the following script to collect the paginated results of the API request into a file:
    
    
    tempFile=$(mktemp)
    nextPageToken=""
    while
        curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages?pageSize=1000&pageToken=$nextPageToken" > $tempFile
        nextPageToken=$(grep nextPageToken $tempFile | sed 's/  "nextPageToken": "//' | sed 's/.$//')
        grep -v nextPageToken $tempFile >> FILENAME7
        [ -n "$nextPageToken" ]
    do
    :
    done
    

### Optional: Write a sorted list of primary Go package names to `FILENAME8`

The following actions filter the returned raw list of Go modules to give you a list of the primary package names:
    
    
    curl -X GET -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages?pageSize=1000" \
          | grep name | sort -f | uniq >  FILENAME8
    

### Optional: Write a sorted list of Go package versions to `FILENAME9`

Even though a direct HTTP request to list all Go package versions is unavailable, you can list all versions of a specific Go package. You can generate a complete list of all Go package versions by iteratively listing the versions of each Go package that's identified in the list in `FILENAME8`.

The following actions filter the returned raw list of Go package versions to give you a list of the package versions:
    
    
    grep -o "packages/.*" FILENAME8 | tr -d '",' | cut -d '/' -f 2 | while read package_name; do curl -X GET -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/assuredoss-go-free/packages/$package_name/versions | grep name | sort -f | uniq >> FILENAME9; done
    

## List all JavaScript (NPM) packages available in Assured OSS

You can use a REST API to list all the JavaScript (NPM) packages and their versions.

For the free tier of Assured OSS, enter the following HTTP request:
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    "https://artifactregistry.googleapis.com/v1/projects/cloud-aoss/locations/us/repositories/assuredoss-javascript-free/packages"
    

For the premium tier of Assured OSS, enter the following HTTP request:
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-javascript/packages
    

Replace PROJECT_ID with the ID of the project that you selected when you set up Assured OSS.

The request returns a response similar to the following:
    
    
    {
      "packages": [
        {
          "name": "projects/cloud-aoss/locations/us/repositories/assuredoss-javascript-free/packages/express",
          "createTime": "2026-06-01T08:00:00.000000Z",
          "updateTime": "2026-06-01T08:00:00.000000Z"
        },
        {
          "name": "projects/cloud-aoss/locations/us/repositories/assuredoss-javascript-free/packages/%40stoplight%2Fspectral-core",
          "createTime": "2026-06-01T08:00:00.000000Z",
          "updateTime": "2026-06-01T08:00:00.000000Z"
        }
      ]
    }
    

If many packages are available, the API response might be paginated. When the listing is incomplete, the continuation token `nextPageToken` is returned in the response.

## What's next

  * [Download Java packages using direct repository access](https://docs.cloud.google.com/assured-open-source-software/docs/download-java-packages)
  * [Download Go packages using direct repository access](https://docs.cloud.google.com/assured-open-source-software/docs/download-go-packages)
  * [Download Python packages using direct repository access](https://docs.cloud.google.com/assured-open-source-software/docs/download-python-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
