---
url: https://docs.cloud.google.com/assured-open-source-software/docs/download-java-packages/
title: Download Java packages using direct repository access for the free tier \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:36.070528+00:00
---

# Download Java packages using direct repository access for the free tier  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/download-java-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Download Java packages using direct repository access for the free tier Stay organized with collections  Save and categorize content based on your preferences. 

In the free tier, Assured Open Source Software packages are hosted in a Google-managed Artifact Registry repository.

This page explains how you can connect to the Artifact Registry repository for Assured OSS to directly access and download the Java packages.

This document applies to the free tier only. For the premium tier, see [Download Java packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-java-packages).

## Before you begin

  1. Request your administrator to grant you the [Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on your organization. You need this permission to get the base64-encoded string of the service account key. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. Configure Assured OSS. For the free tier, submit the [customer enablement form](https://developers.google.com/assured-oss#get-started) to enable access to Assured OSS.

  3. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Assured OSS for the requested service accounts.

  4. [Enable the Artifact Registry API](https://docs.cloud.google.com/artifact-registry/docs/enable-service) for the parent Google Cloud project of the service accounts used to access Assured OSS.

  5. Install the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). If you have installed the Google Cloud CLI previously, make sure you have the latest version by running this command:
         
         gcloud components update
         




## Set up authentication

Artifact Registry supports the following authentication methods:

  * Authentication with a credential helper
  * Authentication with a password



The following sections describe how to set up these authentication methods.

### Authenticate with a credential helper

Artifact Registry provides a [Maven wagon](https://search.maven.org/artifact/com.google.cloud.artifactregistry/artifactregistry-maven-wagon) and a [Gradle plugin](https://plugins.gradle.org/plugin/com.google.cloud.artifactregistry.gradle-plugin) to use as [credential helpers](https://docs.cloud.google.com/artifact-registry/docs/java/authentication#auth-helper). This option provides the most flexibility.

To set up [Application Default Credentials](https://docs.cloud.google.com/docs/authentication#adc), see [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication).

#### Set up your credential helpers

Make the following changes based on the build tool to set up authentication using a credential helper:

###  Maven 
    
    
    <project>
      <build>
        <extensions>
          <extension>
            <groupId>com.google.cloud.artifactregistry</groupId>
            <artifactId>artifactregistry-maven-wagon</artifactId>
            <version>2.2.0</version>
          </extension>
        </extensions>
      </build>
    </project>
    

###  Gradle 
    
    
    plugins {
      id "com.google.cloud.artifactregistry.gradle-plugin" version "2.2.0"
    }
    

### Authenticate using a password

[Authenticate using a password](https://docs.cloud.google.com/artifact-registry/docs/java/authentication#auth-password) when your Java application requires authentication with a specified username and password. Change the settings based on your build tool:

###  Maven 

Add the following authentication settings in the `settings` section of the `~/.m2/settings.xml` file. If the file doesn't already exist, create it. For more information, see the [Maven Settings](https://maven.apache.org/settings.html#Servers) reference. 
    
    
    <settings>
      <servers>
        <server>
          <id>artifact-registry</id>
          <configuration>
            <httpConfiguration>
              <get>
                <usePreemptive>true</usePreemptive>
              </get>
              <head>
                <usePreemptive>true</usePreemptive>
              </head>
              <put>
                <params>
                  <property>
                    <name>http.protocol.expect-continue</name>
                    <value>false</value>
                  </property>
                </params>
              </put>
            </httpConfiguration>
          </configuration>
          <username>_json_key_base64</username>
          <password>KEY</password>
        </server>
      </servers>
    </settings>
    

Replace `KEY` with the base64-encoding of the entire service account JSON key file. To do this, run the following command:
    
    
    cat KEY_FILE_LOCATION  | base64
    

Where KEY_FILE_LOCATION is the location of the service account JSON key file.

###  Gradle 

Add the following line to your `~/.gradle/gradle.properties` file so that the key is not visible in your builds or your source control repository.
    
    
    artifactRegistryMavenSecret = KEY
    

Replace `KEY` with the private key from your service account JSON key file. For `json_key_base64`, the `artifactRegistryMavenSecret` contains the base64 encrypted password. For example, `base64 -w 0 KEY`.

In the `build.gradle` file, specify the repository settings using the following example:
    
    
    repositories {
      maven {
        url "artifactregistry://us-maven.pkg.dev/cloud-aoss/cloud-aoss-java"
        credentials {
          username = "_json_key_base64"
          password = "$artifactRegistryMavenSecret"
        }
        authentication {
          basic(BasicAuthentication)
        }
      }
    }
    

## Update the project configuration file to point to the repository

###  Maven 

Add the following settings to the appropriate section in the `pom.xml` file for your Maven project. Don't replace the authentication settings.
    
    
    <project>
      <repositories>
        <repository>
          <id>artifact-registry</id>
          <url>artifactregistry://us-maven.pkg.dev/cloud-aoss/cloud-aoss-java</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>false</enabled>
          </snapshots>
        </repository>
      </repositories>
    </project>
    

See the Maven [POM reference](https://maven.apache.org/pom.html) for details about the structure of the file.

###  Gradle 

Specify the following repository settings in your `build.gradle` file. Don't replace the authentication settings.
    
    
    repositories {
      maven {
      url "artifactregistry://us-maven.pkg.dev/cloud-aoss/cloud-aoss-java"
      }
    }
    

## Update the project configuration file to add dependencies

To download an artifact as a part of your build, the artifact must be declared as a dependency.

###  Maven 

Declare the packages that you want to download in the `pom.xml` file for your Maven project.
    
    
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-api</artifactId>
        <version>2.17.1</version>
    </dependency>
    

###  Gradle 

Declare the packages that you want to download in your `build.gradle` file.
    
    
    dependencies {
        compile group: 'org.apache.logging.log4j', name: 'log4j-api', version: '2.17.1'
    }
    

## Access Java packages not available in Assured OSS

You can access packages that aren't available in the Artifact Registry repository for Assured OSS.

Assured OSS is pre-configured with Assured OSS as the preferred repository and canonical public repositories, such as Maven Central or PyPI, as secondary repositories. To use the ([Preview](https://cloud.google.com/products#product-launch-stages)) feature, point to the following URL:

`https://us-maven.pkg.dev/cloud-aoss/java`

## List all Java packages available in Assured OSS

To use an [API](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts/list) to get a list of all the Java packages available in the Artifact Registry repository, see [List all Java packages available in Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#list_all_java_packages_available_in).

## What's next

  * [Download Python packages using direct repository access](https://docs.cloud.google.com/assured-open-source-software/docs/download-python-packages)
  * [Set up virtual repository access](https://docs.cloud.google.com/assured-open-source-software/docs/virtual-repository-access)
  * [Supported Java and Python packages](https://docs.cloud.google.com/assured-open-source-software/docs/supported-packages)
  * [Access security metadata using Cloud Storage](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-cloud-storage)
  * [Access security metadata using Artifact Analysis API](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
