---
url: https://docs.cloud.google.com/java/docs/setup/
title: Set up a Java development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:20.170002+00:00
---

# Set up a Java development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Set up a Java development environment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to prepare your local machine for [Java](https://java.com/) development, including developing Java apps that run on Google Cloud. Follow these steps to install Java and relevant tools.

**Tip:** If you want to get started quickly, [Cloud Shell Editor](http://shell.cloud.google.com/) provides IDE support for the full development cycle of Google Kubernetes Engine and Cloud Run applications. Cloud Shell Editor is based on [Code - OSS](https://github.com/microsoft/vscode) and comes with the Google Cloud CLI and Cloud Code tools preinstalled. 

## Objectives

  * Install a JDK (Java Development Kit).
  * Install a build automation tool.
  * Install the gcloud CLI.
  * (Optional) Install an IDE or editor.
  * (Optional) Install IDE Google Cloud plugin.
  * Install the Cloud Client Libraries for Java.
  * Set up authentication.



## Install a JDK (Java Development Kit)

You may choose any Java distribution of your choice by ensuring that the following environment variables are set:

  * JAVA_HOME: Points to the base of the JDK installation.
  * PATH: Includes `$JAVA_HOME/bin`.



[Eclipse Temurin](https://adoptium.net) is the recommended OpenJDK (Java Development Kit) distribution for use with Google Cloud. Temurin is open-source licensed, Java SE TCK-certified, and tested to ensure production-quality performance and security.

### (Recommended) Installing Temurin

Temurin's installation instructions vary by operating system.

  * Binaries are available for [download](https://adoptium.net).
  * For Docker containers, use the [official 'eclipse-temurin' image](https://hub.docker.com/_/eclipse-temurin).



If you are using Compute Engine boot images, you can use the following installation scripts.

### CentOS/RHEL/Rocky

  1. Determine the major version of CentOS/RHEL/Rocky Linux: 
         
         eval "$(grep VERSION_ID /etc/os-release)"
         eval "$(grep ^ID= /etc/os-release)"
         OLD_IFS=$IFS
         IFS='.'
         read -ra split_version <<< "$VERSION_ID"
         IFS=$OLD_IFS
         MAJOR_VERSION=$split_version

  2. Create the Adoptium source repo file, `/etc/yum.repos.d/adoptium.repo`: 
         
         sudo tee /etc/yum.repos.d/adoptium.repo << EOM
         [Adoptium]
         name=Adoptium
         baseurl=https://packages.adoptium.net/artifactory/rpm/$ID/$MAJOR_VERSION/\$basearch
         enabled=1
         gpgcheck=1
         gpgkey=https://packages.adoptium.net/artifactory/api/gpg/key/public
         EOM

  3. Update package lists: 
         
         sudo yum update -y

  4. Install Temurin: 
         
         sudo yum install -y temurin-17-jdk

  5. Verify installation: 
         
         java -version




### Debian/Ubuntu

  1. Install the public repo GPG key. If you are using Ubuntu 16.4, pass the key through `gpg --dearmor` before saving to file. (ex: `sudo wget ... | gpg --dearmor | sudo tee ...`) 
         
         sudo mkdir -p /etc/apt/keyrings
         sudo wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public |
           sudo tee /etc/apt/keyrings/adoptium.asc

  2. Determine the name of the Linux distribution, and create the source list file, `/etc/apt/sources.list.d/adoptium.list`: 
         
         eval "$(grep VERSION_CODENAME /etc/os-release)"
         sudo tee /etc/apt/sources.list.d/adoptium.list << EOM
         deb [signed-by=/etc/apt/keyrings/adoptium.asc] https://packages.adoptium.net/artifactory/deb $VERSION_CODENAME main
         EOM

  3. Update package lists: 
         
         sudo apt update -y

  4. Install Temurin: 
         
         sudo apt install -y temurin-17-jdk

  5. Verify installation: 
         
         java -version




### SLES

  1. Determine the major version of SLES: 
         
         eval "$(grep VERSION_ID /etc/os-release)"
         OLD_IFS=$IFS
         IFS='.'
         read -ra split_version <<< "$VERSION_ID"
         IFS=$OLD_IFS
         MAJOR_VERSION=$split_version

  2. Install the public repository GPG key: 
         
         sudo mkdir -p /etc/zypp/keyrings
         sudo wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public |
           sudo tee /etc/zypp/keyrings/adoptium.asc
         sudo rpm --import /etc/zypp/keyrings/adoptium.asc

  3. Determine the version of SLES, and register the Adoptium repository: 
         
         sudo zypper ar -f "https://packages.adoptium.net/artifactory/rpm/sles/$MAJOR_VERSION/$(uname -m)" adoptium

  4. Update package lists: 
         
         sudo zypper update -y

  5. Install Temurin: 
         
         sudo zypper install -y temurin-17-jdk

  6. Verify installation: 
         
         java -version




### Windows

To install Temurin, run PowerShell version 3.0 or higher as an administrator with the following commands.

  1. Download Temurin. The `Invoke-WebRequest` command in the instructions below requires PowerShell 3.0 or newer. 
         
         $JdkVersion = 17
         $JdkUrl = "https://api.adoptium.net/v3/binary/latest/$JdkVersion/ga/windows/x64/jdk/hotspot/normal/eclipse?project=jdk"
         $JdkExtractionPath = "C:\temurin-$JdkVersion-jdk"
         $JdkDownload = "$JdkExtractionPath.zip"
         [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]'Tls12'
         Invoke-WebRequest -Uri $JdkUrl -OutFile $JdkDownload
         Expand-Archive $JdkDownload -DestinationPath $JdkExtractionPath -Force

  2. Set the `JAVA_HOME` and `Path` variables: 
         
         pushd $JdkExtractionPath
         $JdkPath = (Get-ChildItem).FullName
         popd
         [System.Environment]::SetEnvironmentVariable('JAVA_HOME', $JdkPath, 'Machine')
         
               

  3. (Optional) Refresh your session's `$env:Path` value. Otherwise, start a new session: 
         
         $MachinePath = [System.Environment]::GetEnvironmentVariable('Path', 'Machine')
         $UserPath = [System.Environment]::GetEnvironmentVariable('Path', 'User')
         $env:Path = "$MachinePath;$UserPath"

  4. Verify installation: 
         
         java -version




## Install a build automation tool

[Apache Maven](https://maven.apache.org/install.html), [Gradle](https://gradle.org/), and [SBT](https://www.scala-sbt.org/) are package management options that can help build Java app dependencies quickly and consistently across platforms.

## Install the gcloud CLI

The [gcloud CLI](https://cloud.google.com/sdk/) is a set of tools for Google Cloud. It contains `gcloud` and `bq`, which you can use to access Compute Engine, Cloud Storage, BigQuery, and other products and services from the command line. You can run these tools interactively or in your automated scripts.

## (Optional) Install an IDE or editor

Popular editors (in no particular order) used to develop Java apps include, but are not limited to:

  * [Visual Studio Code](https://code.visualstudio.com/)
  * [IntelliJ IDEA and/or Webstorm](https://www.jetbrains.com/idea/) by JetBrains
  * [Eclipse](https://www.eclipse.org/ide/) by Eclipse Foundation
  * [Atom](https://atom.io/) by GitHub



These editors (sometimes with the help of plugins) give you everything from syntax highlighting, intelli-sense, and code completion to fully integrated debugging capabilities.

## (Optional) Install an IDE plugin

For access to helpful functions within your editor, check out the following plugins:

  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/install)
  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/install)



## Install the Cloud Client Libraries for Java

Use the [Cloud Client Libraries for Java](https://github.com/googleapis/google-cloud-java) to integrate with Google Cloud services, such as Datastore and Cloud Storage. You can install the package for an individual API, such as BigQuery, as shown in the following example.

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <!--  Using libraries-bom to manage versions.
    See https://github.com/GoogleCloudPlatform/cloud-opensource-java/wiki/The-Google-Cloud-Platform-Libraries-BOM -->
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.62.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-bigquery</artifactId>
      </dependency>
    </dependencies>
    

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.45.0')
    
    implementation 'com.google.cloud:google-cloud-bigquery'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-bigquery" % "2.42.2"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Set up authentication

To run the client library, you must first set up authentication.

If you're using a local shell, then create local authentication credentials for your user account: 
    
    
    gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

### Use the client library
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html);
    import com.google.cloud.bigquery.[DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo.html);
    
    public class QuickstartSample {
      public static void main(String... args) throws Exception {
        // Instantiate a client. If you don't specify credentials when constructing a client, the
        // client library will look for credentials in the environment, such as the
        // GOOGLE_APPLICATION_CREDENTIALS environment variable.
        [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
        // The name for the new dataset
        String datasetName = "my_new_dataset";
    
        // Prepares a new dataset
        [Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html) dataset = null;
        [DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo.html) datasetInfo = [DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo.html).newBuilder(datasetName).build();
    
        // Creates the dataset
        dataset = bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(datasetInfo);
    
        System.out.printf("Dataset %s created.%n", dataset.getDatasetId().getDataset());
      }
    }

## Configure endpoints for the client library

If you use APIs that support regional endpoints, use endpoints to configure which server to send requests to. For example, with the [Google.Cloud.Dataproc.V1 API](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1#clustercontrollerclient), you might configure a client endpoint. You can read more about regional endpoints for Dataproc [here](https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints). Be sure to replace MY-PROJECT with your project name and us-central1 with the region appropriate for your configuration in the following example:
    
    
    ClusterControllerSettings settings =
         ClusterControllerSettings.newBuilder()
            .setEndpoint("**us-central1 -dataproc.googleapis.com**:443")
            .build();
     try (ClusterControllerClient clusterControllerClient = ClusterControllerClient.create(settings)) {
       String projectId = "MY-PROJECT";
       String region = "us-central1";
       Cluster cluster = Cluster.newBuilder().build();
     }

## What's next

### (Optional) Use the Maven or Gradle plugin for App Engine

If you are developing in the App Engine standard or flexible environment, you can use plugins for both Apache Maven and Gradle build tools that provide convenient functions for developing, testing, and deploying your apps directly.

#### For App Engine standard environments

Use the [Maven App Engine plugin](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/using-maven) or [Gradle plugin](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/using-gradle) for App Engine standard environments.

#### For App Engine flexible environments

Use the [Maven App Engine plugin](https://docs.cloud.google.com/appengine/docs/flexible/java/using-maven) or [Gradle plugin](https://docs.cloud.google.com/appengine/docs/flexible/java/using-gradle) for App Engine flexible environments.

### More resources

  * Browse the [documentation for Google Cloud products](https://docs.cloud.google.com/products).
  * Clone the [Java samples repository from GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
