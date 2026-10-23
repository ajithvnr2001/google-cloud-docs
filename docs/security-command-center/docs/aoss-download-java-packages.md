---
url: https://docs.cloud.google.com/security-command-center/docs/aoss-download-java-packages/
title: Download Java packages using direct repository access \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:59:32.863798+00:00
---

# Download Java packages using direct repository access  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/aoss-download-java-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Download Java packages using direct repository access Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

After you [integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc), Assured Open Source Software packages are hosted in an Artifact Registry repository that is created in a project that you control.

This page explains how you can connect to the Artifact Registry repository for Assured OSS to directly access and download the Java packages.

This document applies to the Assured OSS premium tier only. For the free tier, see [Download Java packages using direct repository access for the free tier](https://docs.cloud.google.com/assured-open-source-software/docs/download-java-packages).

## Before you begin

  1. Request your administrator to grant you the [Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on your organization. You need this permission to get the base64-encoded string of the service account key. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. [Integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).

  3. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Assured OSS for the requested service accounts.

  4. Install the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). If you have installed the Google Cloud CLI previously, make sure you have the latest version by running this command:
         
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

If you're using a credential helper to set up authentication, make the following changes based on the build tool.

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
    

### Authenticate using password

[Authenticate using password](https://docs.cloud.google.com/artifact-registry/docs/java/authentication#auth-password) when your Java application requires authentication with a specified username and password. Change the settings based on your build tool:

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
    

Replace KEY_FILE_LOCATION with the location of the service account JSON key file.

###  Gradle 

Add the following line to your `~/.gradle/gradle.properties` file so that the key is not visible in your builds or your source control repository.
    
    
    artifactRegistryMavenSecret = KEY
    

Replace `KEY` with the private key from your service account JSON key file. For `json_key_base64`, the `artifactRegistryMavenSecret` contains the base64 encrypted password. For example, `base64 -w 0 KEY`.

In the `build.gradle` file, specify the repository settings using the following example:
    
    
    repositories {
      maven {
        url "artifactregistry://us-maven.pkg.dev/PROJECT_ID/assuredoss-java"
        credentials {
          username = "_json_key_base64"
          password = "$artifactRegistryMavenSecret"
        }
        authentication {
          basic(BasicAuthentication)
        }
      }
    }
    

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured Open Source Software.

## Update the project configuration file to point to the repository

###  Maven 

Add the following settings to the appropriate section in the `pom.xml` file for your Maven project. Don't replace the authentication settings.
    
    
    <project>
      <repositories>
        <repository>
          <id>artifact-registry</id>
          <url>artifactregistry://us-maven.pkg.dev/PROJECT_ID/assuredoss-java</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>false</enabled>
          </snapshots>
        </repository>
      </repositories>
    </project>
    

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured Open Source Software.

See the Maven [POM reference](https://maven.apache.org/pom.html) for details about the structure of the file.

###  Gradle 

Specify the following repository settings in your `build.gradle` file. Don't replace the authentication settings.
    
    
    repositories {
      maven {
      url "artifactregistry://us-maven.pkg.dev/PROJECT_ID/assuredoss-java"
      }
    }
    

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured Open Source Software.

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
    

## List all Java packages available in Assured OSS

To use an [API](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts/list) to get a list of all the Java packages available in the Artifact Registry repository, see [List all Java packages available in Security Command Center](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#list_all_java_packages_available_in).

## What's next

  * [Download Python packages using direct repository access in the premium tier](https://docs.cloud.google.com/security-command-center/docs/aoss-download-python-packages)
  * [Access security metadata and verify packages in the premium tier](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
