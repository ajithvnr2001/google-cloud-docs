---
url: https://docs.cloud.google.com/artifact-registry/docs/java/authentication/
title: Configure authentication to Artifact Registry for Maven and Gradle \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:39.326079+00:00
---

# Configure authentication to Artifact Registry for Maven and Gradle  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/java/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure authentication to Artifact Registry for Maven and Gradle Stay organized with collections  Save and categorize content based on your preferences. 

You must authenticate to Artifact Registry when you use a third-party application to connect to an Artifact Registry repository. This documentation focuses on configuration of Maven and Gradle.

You do not need to configure authentication for Cloud Build or Google Cloud runtime environments such as Google Kubernetes Engine and Cloud Run, but you should verify that the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp) are configured. To learn more, see the information about [Cloud Build](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build) and [deploying](https://docs.cloud.google.com/artifact-registry/docs/deploy) to Google Cloud runtime environments.

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  3. If you are configuring authentication with a standard repository, verify the [version policy](https://docs.cloud.google.com/artifact-registry/docs/java#versions) so that you can configure your Maven project correctly for the types of Java packages you can upload.

###  Console 

     1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

     2. Click the repository that you want to authenticate to.

The **Details** section displays the version policy. If the repository has a snapshot version policy, the **Allow snapshot overwrites** field indicates if snapshots can overwrite matching snapshot versions in the repository.

###  gcloud 

Run the following command to view a description of a repository.
    
    gcloud artifacts repositories describe REPOSITORY \
          --project=PROJECT \
          --location=LOCATION
    

Where

     * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
     * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.

The output of the command includes information about the version policy under `mavenConfig`. In this example, the repository has a snapshot version policy and snapshots cannot overwrite identical versions in the repository.
    
    Encryption: Google-owned and Google-managed encryption key
    createTime: '2021-10-04T19:39:10.897404Z'
    format: MAVEN
    mavenConfig:
      allowSnapshotOverwrites: false
      versionPolicy: SNAPSHOT
    

If a repository does not have a version policy, the value of `mavenConfig` is `{}`.




## Overview

Artifact Registry supports the following authentication methods.

Using an authentication helper
    This option provides the most flexibility. When you include the helper in your Maven or Gradle configuration, Artifact Registry searches for service account credentials in the environment.
Specifying a service account key as a credential
    Use this option when an application does not support Application Default Credentials but does support authentication with a username and password.

Service account keys are long-lived credentials. Use the following guidelines to limit access to your repositories:

  * Consider using a dedicated service account for interacting with repositories.
  * Grant the minimum [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control) required by the service account. For example, assign Artifact Registry Reader to a service account that only downloads artifacts.
  * If groups in your organization require different levels of access to specific repositories, grant access at the repository level rather than the project level.
  * Follow [best practices for managing credentials](https://docs.cloud.google.com/docs/authentication/production#best_practices_for_managing_credentials).



## Authenticating with a credential helper

Artifact Registry provides a [Maven wagon](https://search.maven.org/artifact/com.google.cloud.artifactregistry/artifactregistry-maven-wagon/) and a [Gradle plugin](https://plugins.gradle.org/plugin/com.google.cloud.artifactregistry.gradle-plugin) as credential helpers. When you use the credential helper, your credentials are not stored in your Java project. Instead, Artifact Registry searches for credentials in the following order:

  1. [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/production) (ADC), a strategy that looks for credentials in the following order:

     1. Credentials defined in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

     2. Credentials that the default service account for Compute Engine, Google Kubernetes Engine, Cloud Run, App Engine, or Cloud Run functions provides.

  2. Credentials provided by the Google Cloud CLI, including user credentials from the command `gcloud auth application-default login`.




The `GOOGLE_APPLICATION_CREDENTIALS` variable makes the account for authentication explicit, which makes troubleshooting easier. If you do not use the variable, verify that any accounts that ADC might use have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control). For example the [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for Compute Engine VMs, Google Kubernetes Engine nodes, and Cloud Run revisions has read-only access to repositories. If you intend to upload from these environments using the default service account, you must modify the permissions.

### Set up a service account for a credential helper

To create a service account and set up authentication using the environment variable:

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) a service account to act on behalf of your application, or choose an existing service account that you use for automation.

You will need the location of the service account key file to set up authentication with Artifact Registry. For existing accounts, you can view keys and create new keys on the Service Accounts page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  2. [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the specific [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the service account to provide repository access.

  3. Assign the service account key file location to the variable `GOOGLE_APPLICATION_CREDENTIALS` so that the Artifact Registry credential helper can obtain your key when connecting with repositories.
         
         export GOOGLE_APPLICATION_CREDENTIALS=KEY-FILE
         

Where KEY-FILE is path to the service account [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).




### Configure Maven

  1. Configure Maven for the type of repository you are using.

###  Standard 

     1. Run the following command to print the repository configuration to add to your Java project.
            
            gcloud artifacts print-settings mvn \
                --project=PROJECT \
                --repository=REPOSITORY \
                --location=LOCATION
            

Where

        * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
        * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
        * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
     2. Add the returned settings to the appropriate sections in the `pom.xml` file for your Maven project. See the Maven [POM reference](https://maven.apache.org/pom.html) for details about the structure of the file.

The following example shows settings for a repository that stores both snapshot and release versions.
            
            <distributionManagement>
              <snapshotRepository>
                <id>artifact-registry</id>
                <url>artifactregistry://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY</url>
              </snapshotRepository>
              <repository>
                <id>artifact-registry</id>
                <url>artifactregistry://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY</url>
              </repository>
            </distributionManagement>
            
            <repositories>
              <repository>
                <id>artifact-registry</id>
                <url>artifactregistry://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY</url>
                <releases>
                  <enabled>true</enabled>
                </releases>
                <snapshots>
                  <enabled>true</enabled>
                </snapshots>
              </repository>
            </repositories>
            
            <build>
              <extensions>
                <extension>
                  <groupId>com.google.cloud.artifactregistry</groupId>
                  <artifactId>artifactregistry-maven-wagon</artifactId>
                  <version>2.2.5</version>
                </extension>
              </extensions>
            </build>
            

The `<release>` and `<snapshot>` elements indicate whether the repository stores release packages, snapshot packages, or both. These settings should correspond with the repository [version policy](https://docs.cloud.google.com/artifact-registry/docs/java#versions).

The `<build>` element defines the Artifact Registry wagon as an extension. For information about the wagon, see the documentation for the [Artifact Registry Maven tools](https://github.com/GoogleCloudPlatform/artifact-registry-maven-tools).

###  Remote or virtual

Edit the `pom.xml` file in your project. See the Maven [POM reference](https://maven.apache.org/pom.html) for details about the structure of the file.

The following example shows settings for a remote repository that stores both snapshot and release versions. In this example, the project has a dependency on a version of the Guava package.
    
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
    
      <groupId>com.google.hello</groupId>
      <artifactId>repo-config</artifactId>
      <version>4.1-SNAPSHOT</version>
      <description>version 1 release</description>
    
      <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
      </properties>
      <dependencies>
        <dependency>
          <groupId>com.google.guava</groupId>
          <artifactId>guava</artifactId>
          <version>28.0-jre</version>
        </dependency>
      </dependencies>
    
      <repositories>
        <repository>
          <id>central</id>
          <name>Maven Central remote repository</name>
          <url>artifactregistry://LOCATION-maven.pkg.dev/PROJECT_ID/REMOTE-REPOSITORY-NAME</url>
          <layout>default</layout>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </repository>
      </repositories>
    
      <build>
        <extensions>
          <extension>
            <groupId>com.google.cloud.artifactregistry</groupId>
            <artifactId>artifactregistry-maven-wagon</artifactId>
            <version>2.2.5</version>
          </extension>
        </extensions>
      </build>
    </project>
    

     * The `<repositories>` section defines the Artifact Registry repository. For a remote repository, the `<id>` element must be set to `central`. This setting overrides the default value for the `central` repository ID that is inherited from the [Super POM](https://maven.apache.org/pom.html#The_Super_POM).

     * The `<build>` section sets the Artifact Registry wagon as an extension. For information about the wagon, see the documentation for the [Artifact Registry Maven tools](https://github.com/GoogleCloudPlatform/artifact-registry-maven-tools).

     * In this example, the `<dependencies>` section sets a dependency on the [Guava](https://github.com/google/guava) package version `28.0-jre`.

  2. Maven resolves some dependencies before applying a wagon defined in `pom.xml`, including:

     * References in a child Maven project to a parent project using the `<parent>` element.
     * Plugin dependencies stored in Artifact Registry.

If your project needs to resolve these dependencies, you must use the [core extensions](https://maven.apache.org/docs/3.3.1/release-notes.html) mechanism to ensure that Maven can locate parent POM files and plugins.

In your project, create the file `${maven.projectBasedir}/.mvn/extensions.xml` with the following content. The `<extension>` element defines the wagon.
    
    <extensions xmlns="http://maven.apache.org/EXTENSIONS/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/EXTENSIONS/1.0.0 http://maven.apache.org/xsd/core-extensions-1.0.0.xsd">
      <extension>
        <groupId>com.google.cloud.artifactregistry</groupId>
        <artifactId>artifactregistry-maven-wagon</artifactId>
        <version>2.2.5</version>
      </extension>
    </extensions>
    

Maven can now resolve parent or plugin dependencies from Artifact Registry.




Your authentication configuration is complete.

### Configure Gradle

  1. Configure Gradle for the type of repository you are using.

###  Standard 

     1. Run the following command to print the repository configuration to add to your Java project.
            
            gcloud artifacts print-settings gradle \
                --project=PROJECT \
                --repository=REPOSITORY \
                --location=LOCATION
            

Where

        * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
        * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
        * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
     2. Add the repository settings to your `build.gradle` file. The following example shows the relative location of the printed sections.
            
            plugins {
              id "maven-publish"
              id "com.google.cloud.artifactregistry.gradle-plugin" version "2.2.5"
            }
            
            publishing {
              publications {
                mavenJava(MavenPublication) {
                  groupId 'maven.example.id'
                  from components.java
                 }
              }
              repositories {
                maven {
                  url "artifactregistry://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY"
                }
              }
            }
            repositories {
              maven {
                url "artifactregistry://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY"
              }
            }
            

        * The `plugins` section declares the Artifact Registry plugin. For information about the plugin, see the documentation for the [Artifact Registry Maven tools](https://github.com/GoogleCloudPlatform/artifact-registry-maven-tools).

        * The `publishing` section defines the files to upload and the target Artifact Registry repository. You can update the file list in the `publications` section when you are ready to upload. For information about publishing settings, see the [Maven Publish plugin](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:repositories) documentation.

###  Remote or virtual 

Add the repository settings to your `build.gradle` file.

The following example shows settings for a remote repository. In this example, the project has a dependency on a version of the Guava package.
    
    plugins {
      id 'java'
      id "maven-publish"
      id "com.google.cloud.artifactregistry.gradle-plugin" version "2.2.5"
      id 'maven'
    }
    
    repositories {
      maven {
        url "artifactregistry://LOCATION-maven.pkg.dev /PROJECT_ID/REMOTE-REPOSITORY-NAME"
      }
    }
    dependencies {
      compile "com.google.guava:guava:31.1-jre"
    }
    

     * The `plugins` section declares the Artifact Registry plugin. For information about the plugin, see the documentation for the [Artifact Registry Maven tools](https://github.com/GoogleCloudPlatform/artifact-registry-maven-tools).

     * The `repositories` section defines the Artifact Registry repository.

     * In this example, the `dependencies` section sets a dependency on the [Guava](https://github.com/google/guava) package version `31.1-jre`.

[Define your dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies.html) for your package in the `dependencies` section.

  2. If you need to use repositories in your `init.gradle` or `settings.gradle` file, you can add the plugin configuration to those files.

For `init.gradle`, add the following configuration:
         
         initscript {
           repositories {
             maven {
               url "https://plugins.gradle.org/m2/"
             }
           }
           dependencies {
             classpath "gradle.plugin.com.google.cloud.artifactregistry:artifactregistry-gradle-plugin:2.2.5"
           }
         }
         apply plugin: com.google.cloud.artifactregistry.gradle.plugin.ArtifactRegistryGradlePlugin
         

For settings.gradle, add the following configuration:
         
         buildscript {
           repositories {
             maven {
               url "https://plugins.gradle.org/m2/"              }
             }
           dependencies {
             classpath "gradle.plugin.com.google.cloud.artifactregistry:artifactregistry-gradle-plugin:2.2.5"
           }
         }
         apply plugin: "com.google.cloud.artifactregistry.gradle-plugin"
         




Your authentication configuration is complete.

## Configuring password authentication

Use this approach when your Java application requires authentication with a specified username and password.

### Set up a service account for password authentication

To create a service account:

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) a service account to act on behalf of your application, or choose an existing service account that you use for automation.

You will need the location of the service account key file to set up authentication with Artifact Registry. For existing accounts, you can view keys and create new keys on the Service Accounts page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  2. If you want to activate the service account in the current gcloud CLI session, run the command:
         
         gcloud auth activate-service-account ACCOUNT --key-file=KEY-FILE
         

Where

     * ACCOUNT is the user or service account.
     * KEY-FILE is path to the service account JSON [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).



### Configure Maven

  1. Configure Maven for the type of repository you are using.

###  Standard 

     1. Run the following command to print the repository configuration to add to your Java project.
            
            gcloud artifacts print-settings mvn \
                --project=PROJECT \
                --repository=REPOSITORY \
                --location=LOCATION \
                --json-key=KEY-FILE
            

Where

        * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
        * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
        * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
        * KEY-FILE is path to the service account JSON [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

The command returns settings to include in your Java project, including a base64-encoded version of your private key.

**Note:** If you choose to set up password authentication using an approach that is not described in these instructions, ensure that you base64 encode your private key. For example, you can use the command `base64 -w 0 KEY-FILE`.
     1. Add the returned repository settings in the `<project>` element to the appropriate sections of the `pom.xml` file for your Maven project. See the Maven [POM reference](https://maven.apache.org/pom.html) for details about the structure of the file.
    
    <project>
      <distributionManagement>
        <snapshotRepository>
          <id>artifact-registry</id>
          <url>https://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY</url>
        </snapshotRepository>
        <repository>
          <id>artifact-registry</id>
          <url>https://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY</url>
        </repository>
      </distributionManagement>
    
      <repositories>
        <repository>
          <id>artifact-registry</id>
          <url>https://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </repository>
      </repositories>
    </project>
    

The `<release>` and `<snapshot>` elements indicate whether the repository stores release packages, snapshot packages, or both. These settings should correspond with the repository [version policy](https://docs.cloud.google.com/artifact-registry/docs/java#versions).

     1. Add the returned authentication settings in the `<settings>` element to the `<servers>` section of the `~/.m2/settings.xml` file. In the following example, `KEY` is the base64-encoded key from your key file.

See the Maven [Settings reference](https://maven.apache.org/settings.html#Servers) for more information.
    
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
    

###  Remote or virtual 

     1. Add the repository settings to the appropriate sections of the `pom.xml` file for your Maven project. See the Maven [POM reference](https://maven.apache.org/pom.html) for details about the structure of the file.
            
            <repositories>
              <repository>
                 <id>central</id>
                 <name>Maven Central remote repository</name>
                 <url>artifactregistry://LOCATION-maven.pkg.dev/PROJECT_ID/REMOTE-REPOSITORY-NAME</url>
                 <layout>default</layout>
                 <releases>
                   <enabled>true</enabled>
                 </releases>
                 <snapshots>
                  <enabled>true</enabled>
                </snapshots>
              </repository>
            </repositories>
            

The `<repositories>` section defines the Artifact Registry repository. For a remote repository, the `<id>` element must be set to `central`. This setting overrides the default value for the `central` repository ID that is inherited from the [Super POM](https://maven.apache.org/pom.html#The_Super_POM).

     1. Base64 encode your key file with the following command. Replace KEY-FILE with the name of your key file.
            
            base64 -w 0 KEY-FILE
            

     2. Add authentication settings in the `<settings>` element to the `<servers>` section of the `~/.m2/settings.xml` file.

See the Maven [Settings reference](https://maven.apache.org/settings.html#Servers) for more information.
    
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
    

**Note:** If you choose to set up password authentication using an approach that is not described in these instructions, ensure that you base64 encode your private key. For example, you can use the command `base64 -w 0 KEY-FILE`.
     1. If you are using HTTP endpoints and want to use [Maven native](https://maven.apache.org/guides/mini/guide-resolver-transport.html#switching-between-transports) connectivity to authenticate, you can pass an authentication header using a [Custom HTTP](https://maven.apache.org/guides/mini/guide-resolver-transport.html#switching-between-transports:%7E:text=or%20wagon%20values.-,Custom%20HTTP%20Headers,-In%20all%20HTTP) header in the `settings.xml`.

Example:
    
    <settings>
    <servers>
      <server>
        <id>artifact-registry</id>
        <configuration>
          <httpHeaders>
            <property>
              <name>Authorization </name>
              <value>Bearer ${artifact.registry.token}</value>
            </property>
          </httpHeaders>
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
      </server>
    </servers>
    </settings>
    

**Note:** To use the authentication header value with a Maven based deployment, set a TOKEN variable `TOKEN=$(gcloud auth print-access-token)` and use the following local Java environment flag as part of the deployment command: `mvn clean deploy -Dartifact.registry.token=$TOKEN`




Your authentication configuration is complete.

### Configure Gradle

  1. Configure Gradle for the type of repository you are using.

###  Standard 

     1. Run the following command to print the repository configuration to add to your Java project.
            
            gcloud artifacts print-settings gradle \
                --project=PROJECT \
                --repository=REPOSITORY \
                --location=LOCATION \
                --json-key=KEY-FILE
            

Where

        * PROJECT is the project ID.
        * REPOSITORY is the ID or fully qualified identifier for the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
        * KEY-FILE is path to the service account JSON [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys). If you ran the command to activate your service account, you can omit this flag.

The command returns settings to include in your Java project, including a base64-encoded version of your private key.

     2. The following line from the returned configuration defines a variable named `artifactRegistryMavenSecret` for your service account key. Add this line to your `~/.gradle/gradle.properties` file so that the key is not visible in your builds or your source control repository.
            
            artifactRegistryMavenSecret = KEY
            

In this line, KEY is the private key in your service account key file. For `_json_key_base64`, `artifactRegistryMavenSecret` is set to the base64-encoded key as your password.

     3. In your `build.gradle` specify the repository settings:
            
            plugins {
              id "maven-publish"
            }
            
            publishing {
              publications {
                mavenJava(MavenPublication) {
                  groupId 'maven.example.id'
                  from components.java
                }
              }
              repositories {
                maven {
                  url "https://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY"
                  credentials {
                    username = "_json_key_base64"
                    password = "$artifactRegistryMavenSecret"
                  }
                  authentication {
                    basic(BasicAuthentication)
                  }
                }
              }
            }
            repositories {
              maven {
                url "https://LOCATION-maven.pkg.dev/PROJECT/REPOSITORY"
                credentials {
                  username = "_json_key_base64"
                  password = "$artifactRegistryMavenSecret"
                }
                authentication {
                  basic(BasicAuthentication)
                }
              }
            }
            

        * The `repositories` section sets the repository URL and credentials for authentication.
        * The `publishing` section defines the files to upload and the target Artifact Registry repository. You can update the file list in the `publications` section when you are ready to upload. For information about publishing settings, see the [Maven Publish plugin](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:repositories) documentation.

###  Remote or virtual 

     1. Base64 encode your key file with the following command. Replace KEY-FILE with the name of your key file.
            
            base64 -w 0 KEY-FILE
            

     2. In the file `~/.gradle/gradle.properties`, add the following line so that your key is not visible in your builds or your source control repository.
            
            artifactRegistryMavenSecret = KEY
            

In this line, KEY is the content of your base64-encoded key file.

     3. Add the repository settings to your `build.gradle` file.

The following example shows configuration of a remote repository.
    
    plugins {
      id 'java'
      id "maven-publish"
      id 'maven'
    }
    
    repositories {
      maven {
        url "artifactregistry://LOCATION-maven.pkg.dev /PROJECT_ID/REMOTE-REPOSITORY-NAME"
        credentials {
        username = "_json_key_base64"
        password = "$artifactRegistryMavenSecret"
      }
      authentication {
        basic(BasicAuthentication)
      }
      dependencies {
        compile "com.google.guava:guava:31.1-jre"
      }
    

     * The `repositories` section defines the Artifact Registry repository.

     * In this example, the `dependencies` section sets a dependency on the [Guava](https://github.com/google/guava) package version `31.1-jre`.

[Define your dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies.html) for your package in the `dependencies` section.




Your authentication configuration is complete.

## What's next

  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories)
  * [Manage packages](https://docs.cloud.google.com/artifact-registry/docs/java/manage-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
