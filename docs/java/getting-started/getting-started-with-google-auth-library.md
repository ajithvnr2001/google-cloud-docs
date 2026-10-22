---
url: https://docs.cloud.google.com/java/getting-started/getting-started-with-google-auth-library/
title: Get started with Google Auth Library \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:46.596990+00:00
---

# Get started with Google Auth Library  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/getting-started/getting-started-with-google-auth-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Get started with Google Auth Library Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Google Auth Library is an open source authentication client library for Java. This document describes how to use this library to authenticate your Java applications to access Google Cloud services.

By following this guide, you will learn how to:

  * Add the necessary Auth Library dependencies to your project using Maven, Gradle, or Simple Build Tool (SBT).
  * Authenticate using various methods, with a focus on Application Default Credentials (ADC).
  * Configure advanced authentication scenarios, including Workload Identity Federation, Workforce Identity Federation, and service account impersonation.
  * Generate and use downscoped tokens to limit permissions.
  * Integrate credentials with Google HTTP client libraries.



This documentation is intended for Java developers. For complete API details, refer to the [Google Auth Library API Documentation](https://googleapis.dev/java/google-auth-library/latest).

The Google Auth Library for Java consists of four artifacts:

  * **`google-auth-library-credentials`** contains base classes and interfaces for Google credentials.
  * **`google-auth-library-appengine`** contains App Engine credentials and depends on the App Engine SDK.
  * **`google-auth-library-oauth2-http`** contains a variety of credentials and utility methods, including capabilities to get Application Default Credentials. It also provides the server-side approach for generating downscoped tokens.
  * **`google-auth-library-cab-token-generator`** provides the client-side approach for generating downscoped tokens.



## Validate credential configurations

When you use credential configurations, such as JSON, file paths, or streams, from an external source, you must validate them. Providing unvalidated credentials to Google APIs or client libraries for authentication to Google Cloud can compromise the security of your systems and data.

For more information, see [Externally sourced credentials](https://docs.cloud.google.com/java/docs/authentication/external/externally-sourced-credentials). Default Credentials.

## Import the Auth Library

To import the Auth Library, use `com.google.cloud:libraries-bom` or use the Google Auth Library Bill of Materials with Maven or Gradle.

### Java SDK libraries-bom

To authenticate to a client library in the Java SDK (for example, `google-cloud-datastore`) using the Auth Library, use `libraries-bom`, which will pull in the versions of Auth Library compatible with that client library.

For example, to import the Auth Library with Maven using a `pom.xml`:
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.53.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    

If you don't use `libraries-bom` or other client libraries, import the Auth modules directly with the Google Auth Library Bill of Materials.

### Google Auth Library Bill of Materials

You can use the Google Auth Library Bill of Materials to ensure that the Auth modules and relevant transitive dependencies are compatible.

#### Maven

Add the following to your `pom.xml` file:
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.auth</groupId>
          <artifactId>google-auth-library-bom</artifactId>
          <version>1.30.1</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    

In the `<dependencies>` section, you can specify any of the Auth modules that are needed. For example, to include the `google-auth-library-oauth2-http` module, add the following `<dependency>` item:
    
    
    <dependency>
      <groupId>com.google.auth</groupId>
      <!-- Let the BOM manage the module and dependency versions -->
      <!-- Replace with the module(s) that are needed -->
      <artifactId>google-auth-library-oauth2-http</artifactId>
    </dependency>
    

Replace `google-auth-library-oauth2-http` in the example with `google-auth-library-credentials` or `google-auth-library-appengine`, depending on your application needs.

#### Gradle

Similar to Maven, Gradle users can use the `google-auth-library-bom` to manage dependency versions and ensure compatibility between the different `google-auth-library` modules.

To use the BOM with Gradle, add the BOM as a `platform` dependency. Then, add the `google-auth-library` modules that you need. The BOM ensures that the versions of all the modules you use are compatible. For example, add the following to your `build.gradle` file:
    
    
    dependencies {
        // The BOM will manage the module versions and transitive dependencies
        implementation platform('com.google.auth:google-auth-library-bom:1.30.1')
        // Replace with the module(s) that are needed
        implementation 'com.google.auth:google-auth-library-oauth2-http'
    }
    
    

#### Scala

Unlike Maven and Gradle, SBT (Scala Build Tool) does not support Maven Bills of Materials (BOMs). As a result, when using Scala, you cannot import the `google-auth-library-bom` to automatically handle compatible versions of the Auth Library modules and their transitive dependencies.

Instead, you'll need to add each required submodule directly to your `build.sbt` file. It's critical to explicitly specify and align the versions of all `google-auth-library` modules you are using. Failing to keep the versions consistent can lead to version conflicts among transitive dependencies, potentially causing unexpected behavior or runtime errors in your application.

Add this to your dependencies if using SBT:
    
    
    // Replace this with the implementation module that suits your needs
    libraryDependencies += "com.google.auth" % "google-auth-library-oauth2-http" % "1.30.1"
    

## Auth Library Logging

The Java Auth Library recommends logging using [client library debug logging](https://docs.cloud.google.com/java/docs/troubleshooting.md#client_library_debug_logging_slf4j). Debug logging will hash sensitive tokens (e.g. access_token, refresh_token, etc) and the values will be masked. Logging with `java.util.logging` is disabled in the Auth Library to prevent leaking of sensitive tokens.

Client debug logging functionality is [opt-in](https://docs.cloud.google.com/java/docs/troubleshooting.md#enable_logging_with_an_environment_variable) and requires [setup](https://docs.cloud.google.com/java/docs/troubleshooting#prerequisite).

Debug Logging can log the following based on log level:

  * Request Information: Headers, URL, Method (INFO Level)
  * Response Information: Headers, Status, Message (INFO level)
  * Response Payload (DEBUG level)



## Migrate from `GoogleCredential` to `GoogleCredentials`

[`GoogleCredential`](https://docs.cloud.google.com/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential) from `google-api-java-client` is deprecated and `GoogleCredentials` is the recommended replacement.

Instantiate `GoogleCredentials` using [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials). This is the recommended approach:
    
    
    GoogleCredentials credentials = GoogleCredentials.getApplicationDefault();
    

The way you use `GoogleCredentials` depends on the client library:

  * **[Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#cloud-client-libraries):** These libraries automatically use Application Default Credentials (ADC), so you don't need to provide credentials in your code.

  * **[Google API Client Libraries](https://docs.cloud.google.com/java/apis/docs/client-libraries-explained#google-api-client-libraries):** You must instantiate `GoogleCredentials` and pass them to the client. For an example, see the [Google API Java Client Guide](https://developers.google.com/api-client-library/java/google-api-java-client/requests).




## Application Default Credentials

The Google Auth Library provides an implementation of [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) for Java. ADC provide a way to get authorization credentials to call Google APIs.

Use ADC when your application requires a consistent identity and authorization level, independent of the user. We recommend using ADC to authorize calls to Cloud APIs, especially when building applications on Google Cloud.

ADC also supports Workload Identity Federation, enabling applications to access Google Cloud resources from external platforms like Amazon Web Services (AWS), Microsoft Azure, or any identity provider that supports OpenID Connect (OIDC). We recommend workload identity federation for non-Google Cloud environments because it eliminates the need to download, manage, and store service account private keys locally.

### Get Application Default Credentials

To get Application Default Credentials, use `GoogleCredentials.getApplicationDefault()` or `GoogleCredentials.getApplicationDefault(HttpTransportFactory)`. These methods return Application Default Credentials to identify and authorize the whole application.

The following are searched, in this order, to find the Application Default Credentials:

  1. Credentials file pointed to by the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
  2. Credentials provided by the Google Cloud SDK `gcloud auth application-default login` command.
  3. Google App Engine built-in credentials.
  4. Google Cloud Shell built-in credentials.
  5. Google Compute Engine built-in credentials. 
     * Skip this check by setting the environment variable `NO_GCE_CHECK=true`.
     * Customize the metadata server address by setting the environment variable `GCE_METADATA_HOST=<hostname>`.



### Explicit credential loading

To get credentials from a Service Account JSON key, use `GoogleCredentials.fromStream(InputStream)` or `GoogleCredentials.fromStream(InputStream, HttpTransportFactory)` as shown in the following example code.

The credentials must be refreshed before the access token is available.
    
    
    GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("/path/to/credentials.json"));
    credentials.refreshIfExpired();
    AccessToken token = credentials.getAccessToken();
    // OR
    AccessToken token = credentials.refreshAccessToken();
    

### Impersonated credentials

Use `ImpersonatedCredentials` to allow a credential (the principal) to impersonate a service account (the target). This lets the principal access resources as the target, without needing the target's private key.

To use `ImpersonatedCredentials`, you must meet the following requirements:

  * The principal's project must have the `IAMCredentials` API enabled.
  * The principal must have the `Service Account Token Creator` (Identity and Access Management) role on the target service account.



The following code sample creates `ImpersonatedCredentials`. The principal's credential is obtained from Application Default Credentials (ADC). The resulting `ImpersonatedCredentials` are then used to access Google Cloud Storage as the target service account.
    
    
    // The principal (ADC) has the Service Account Token Creator role on the target service account.
    GoogleCredentials sourceCredentials =
        GoogleCredentials.getApplicationDefault()
            .createScoped(Arrays.asList("https://www.googleapis.com/auth/iam"));
    
    ImpersonatedCredentials credentials =
        ImpersonatedCredentials.newBuilder()
            .setSourceCredentials(sourceCredentials)
            .setTargetPrincipal(
                "impersonated-account@project.iam.gserviceaccount.com")
            .setScopes(Arrays.asList("https://www.googleapis.com/auth/devstorage.read_only"))
            .build();
    
    Storage storage =
        StorageOptions.newBuilder().setProjectId("project-id").setCredentials(credentials).build()
            .getService();
    
    for (Bucket b : storage.list().iterateAll()) {
      System.out.println(b);
    }
    

## Workload Identity Federation

Workload Identity Federation lets your application access Google Cloud resources from Amazon Web Services (AWS), Microsoft Azure, or any identity provider that supports OpenID Connect (OIDC).

Conventionally, applications running outside Google Cloud have used service account keys to access Google Cloud resources. Using identity federation, your workload can impersonate a service account. This lets the external workload access Google Cloud resources directly, eliminating the maintenance and security burden associated with service account keys.

### Access resources from AWS

To access Google Cloud resources from Amazon Web Services (AWS), you must first configure workload identity federation. The setup process is detailed in [Accessing resources from AWS](https://docs.cloud.google.com/iam/docs/access-resources-aws).

As part of that process, you will generate a credential configuration file. This file contains non-sensitive metadata that instructs the library how to retrieve external subject tokens and exchange them for service account access tokens. You can generate the file using the [Google Cloud CLI](https://cloud.google.com/cli/):
    
    
    # Generate an AWS configuration file.
    gcloud iam workload-identity-pools create-cred-config \
        projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>AWS_PROVIDER_ID</var> \
        --service-account <var>SERVICE_ACCOUNT_EMAIL</var> \
        --aws \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`POOL_ID`:** the workload identity pool ID.
  * **`AWS_PROVIDER_ID`:** the AWS provider ID.
  * **`SERVICE_ACCOUNT_EMAIL`:** the email of the service account to impersonate.



The example generates the configuration file in the specified output file.

If you are using [AWS IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) , you need to add an additional flag `--enable-imdsv2` to the `gcloud iam workload-identity-pools create-cred-config` command:
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/AWS_PROVIDER_ID \
        --service-account SERVICE_ACCOUNT_EMAIL \
        --aws \
        --output-file /path/to/generated/config.json \
        --enable-imdsv2
    

You can now use the Auth library to call Google Cloud resources from AWS.

### Access resources from Microsoft Azure

To access Google Cloud resources from Microsoft Azure, you must first configure workload identity federation. The setup process is detailed in [Accessing resources from Azure](https://docs.cloud.google.com/iam/docs/access-resources-azure).

As part of that process, you will generate a credential configuration file. This file contains non-sensitive metadata that instructs the library how to retrieve external subject tokens and exchange them for service account access tokens. You can generate the file using the [Google Cloud CLI](https://cloud.google.com/cli/):
    
    
    # Generate an Azure configuration file.
    gcloud iam workload-identity-pools create-cred-config \
        projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>AZURE_PROVIDER_ID</var> \
        --service-account <var>SERVICE_ACCOUNT_EMAIL</var> \
        --azure \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`POOL_ID`:** the workload identity pool ID.
  * **`AZURE_PROVIDER_ID`:** the Azure provider ID.
  * **`SERVICE_ACCOUNT_EMAIL`:** the email of the service account to impersonate.



This command generates the configuration file in the specified output file.

You can now use the Auth library to call Google Cloud resources from Azure.

### Access resources from an OIDC identity provider

To access Google Cloud resources from an identity provider that supports [OpenID Connect (OIDC)](https://openid.net/connect/), you must first configure workload identity federation as detailed in [Configuring workload identity federation from an OIDC identity provider](https://docs.cloud.google.com/iam/docs/access-resources-oidc).

As part of that process, you will generate a credential configuration file using the [Google Cloud CLI](https://cloud.google.com/cli/). This file contains non-sensitive metadata that instructs the library how to retrieve external subject tokens and exchange them for service account access tokens.

For OIDC providers, the Auth library can retrieve OIDC tokens from a local file (file-sourced credentials), a local server (URL-sourced credentials), or a X.509 certificate and private-key combination (X.509 certificate-sourced credentials).

### File-sourced credentials

For file-sourced credentials, a background process must continuously refresh the file location with a new OIDC token prior to expiration. For tokens with one hour lifetimes, you need to update the token in the file every hour. You can store the token directly as plain text or in JSON format.

To generate a file-sourced OIDC configuration, run the following command:
    
    
    # Generate an OIDC configuration file for file-sourced credentials.
    gcloud iam workload-identity-pools create-cred-config \
        projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>OIDC_PROVIDER_ID</var> \
        --service-account <var>SERVICE_ACCOUNT_EMAIL</var> \
        --credential-source-file <var>PATH_TO_OIDC_ID_TOKEN</var> \
        # Optional arguments for file types. Default is "text":
        # --credential-source-type "json" \
        # Optional argument for the field that contains the OIDC credential.
        # This is required for json.
        # --credential-source-field-name "id_token" \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`POOL_ID`:** the workload identity pool ID.
  * **`OIDC_PROVIDER_ID`:** the OIDC provider ID.
  * **`SERVICE_ACCOUNT_EMAIL`:** the email of the service account to impersonate.
  * **`PATH_TO_OIDC_ID_TOKEN`:** the path used to retrieve the OIDC token.



This command generates the configuration file in the specified output file.

### URL-sourced credentials

For URL-sourced credentials, a local server must host a GET endpoint that provides an OIDC token in plain text or JSON format. You can specify additional HTTP headers to send in the token request, if required by the endpoint.

To generate a URL-sourced OIDC workload identity configuration, run the following command:
    
    
    # Generate an OIDC configuration file for URL-sourced credentials.
    gcloud iam workload-identity-pools create-cred-config \
        projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>OIDC_PROVIDER_ID</var> \
        --service-account <var>SERVICE_ACCOUNT_EMAIL</var> \
        --credential-source-url <var>URL_TO_GET_OIDC_TOKEN</var> \
        --credential-source-headers <var>HEADER_KEY=HEADER_VALUE</var> \
        # Optional arguments for file types. Default is "text":
        # --credential-source-type "json" \
        # Optional argument for the field that contains the OIDC credential.
        # This is required for json.
        # --credential-source-field-name "id_token" \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`POOL_ID`:** the workload identity pool ID.
  * **`OIDC_PROVIDER_ID`:** the OIDC provider ID.
  * **`SERVICE_ACCOUNT_EMAIL`:** the email of the service account to impersonate.
  * **`URL_TO_GET_OIDC_TOKEN`:** the URL of the local server endpoint to call to retrieve the OIDC token.
  * **`HEADER_KEY` and `HEADER_VALUE`**: the additional header key and value pairs to pass along the GET request to `URL_TO_GET_OIDC_TOKEN`, for example `Metadata-Flavor=Google`.



You can now use the Auth library to call Google Cloud resources from an OIDC provider.

### Access resources using X.509 certificate-sourced credentials

For X.509 certificate-sourced credentials, the authentication library uses an X.509 certificate and private key to prove your application's identity. X.509 certificates include an expiration date and must be renewed before they expire to maintain access.

For more information, see the [official documentation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates).

#### Generate configuration files for X.509 federation

To configure X.509 certificate-sourced credentials, you generate two separate files: a primary credential configuration file and a certificate configuration file.

  * The primary credential configuration file contains the necessary metadata for authentication. This file also references the certificate configuration file.
  * The certificate configuration file specifies the file paths for the X.509 certificate, private key, and trust chain.



The [`gcloud iam workload-identity-pools create-cred-config`](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config) command can be used to create both.

The location where `gcloud` creates the certificate configuration file depends on whether you use the `--credential-cert-configuration-output-file` flag.

#### Default behavior (recommended)

If you omit the `--credential-cert-configuration-output-file` flag, `gcloud` creates the certificate configuration file at a default, well-known location that the Auth library can automatically discover. This approach is suitable for most use cases. The default credential configuration file is named `config.json` and the default certificate configuration file is named `certificate_config.json`.

For example, run the following command to create the configuration files using the default behavior:
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>PROVIDER_ID</var> \
        --service-account <var>SERVICE_ACCOUNT_EMAIL</var> \
        --credential-cert-path "<var>PATH_TO_CERTIFICATE</var>" \
        --credential-cert-private-key-path "<var>PATH_TO_PRIVATE_KEY</var>" \
        --credential-cert-trust-chain-path "<var>PATH_TO_TRUST_CHAIN</var>" \
        --output-file /path/to/config.json
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`POOL_ID`:** the workload identity pool ID.
  * **`PROVIDER_ID`:** the provider ID.
  * **`SERVICE_ACCOUNT_EMAIL`:** the email of the service account to impersonate.
  * **`PATH_TO_CERTIFICATE`:** the path where your leaf X.509 certificate is located.
  * **`PATH_TO_PRIVATE_KEY`:** the path where the corresponding private key for the leaf certificate is located.
  * **`PATH_TO_TRUST_CHAIN`:** the path of the X.509 certificate trust chain file. This file should be a PEM-formatted file containing any intermediate certificates required to complete the trust chain between the leaf certificate and the trust store configured in the Workload Identity Federation pool. The leaf certificate is optional in this file.



This command results in the following:

  * **`/path/to/config.json`:** Created at the path you specified. This file will contain `"use_default_certificate_config": true` to instruct clients to look for the certificate configuration at the default path.
  * **`certificate_config.json`:** Created at the default Google Cloud CLI configuration path, which is typically `~/.config/gcloud/certificate_config.json` on Linux and macOS, or `%APPDATA%\gcloud\certificate_config.json` on Windows.



#### Custom location behavior

If you need to store the certificate configuration file in a non-default location, use the `--credential-cert-configuration-output-file` flag.

Example command (custom location):
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>PROVIDER_ID</var> \
        --service-account <var>SERVICE_ACCOUNT_EMAIL</var> \
        --credential-cert-path "<var>PATH_TO_CERTIFICATE</var>" \
        --credential-cert-private-key-path "<var>PATH_TO_PRIVATE_KEY</var>" \
        --credential-cert-trust-chain-path "<var>PATH_TO_TRUST_CHAIN</var>" \
        --credential-cert-configuration-output-file "/custom/path/cert_config.json" \
        --output-file /path/to/config.json
    

This command results in:

  * **`/path/to/config.json`:** created at the path you specified. This file will contain a `"certificate_config_location"` field that points to your custom path.
  * **`cert_config.json`:** created at `/custom/path/cert_config.json`, as specified by the flag.



You can now use the Auth library to call Google Cloud resources with X.509 certificate-sourced credentials.

### Use executable-sourced credentials with OIDC and SAML

For executable-sourced credentials, a local executable is used to retrieve the third-party token. The executable must provide a valid, unexpired OIDC ID token or SAML assertion in JSON format to `stdout`.

To use executable-sourced credentials, the `GOOGLE_EXTERNAL_ACCOUNT_ALLOW_EXECUTABLES` environment variable must be set to `1`.

To generate an executable-sourced workload identity configuration, run the following command:
    
    
    # Generate a configuration file for executable-sourced credentials.
    gcloud iam workload-identity-pools create-cred-config \
        projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>PROVIDER_ID</var> \
        --service-account=<var>SERVICE_ACCOUNT_EMAIL</var> \
        --subject-token-type=<var>SUBJECT_TOKEN_TYPE</var> \
        # The absolute path for the program, including arguments.
        # e.g. --executable-command="/path/to/command --foo=bar"
        --executable-command=<var>EXECUTABLE_COMMAND</var> \
        # Optional argument for the executable timeout. Defaults to 30s.
        # --executable-timeout-millis=<var>EXECUTABLE_TIMEOUT</var> \
        # Optional argument for the absolute path to the executable output file.
        # See below on how this argument impacts the library behaviour.
        # --executable-output-file=<var>EXECUTABLE_OUTPUT_FILE</var> \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`POOL_ID`:** the workload identity pool ID.
  * **`PROVIDER_ID`:** the OIDC or SAML provider ID.
  * **`SERVICE_ACCOUNT_EMAIL`:** the email of the service account to impersonate.
  * **`SUBJECT_TOKEN_TYPE`:** the subject token type.
  * **`EXECUTABLE_COMMAND`:** the full command to run, including arguments. Must be an absolute path to the program.



The `--executable-timeout-millis` flag is optional; it specifies the duration (in milliseconds) for which the Auth library will wait for the executable to finish. If not provided, it defaults to 30 seconds. The maximum allowed value is two minutes, and the minimum is five seconds.

The optional `--executable-output-file` flag specifies a path to cache the executable's third-party credential response. Caching helps improve performance because the auth libraries first check this file for valid, unexpired credentials before running the executable. If valid, cached credentials exist, the libraries use them, avoiding unnecessary executable runs.

Your executable must write the credential response to this file. The auth libraries only read from this location. The file's content must match the expected JSON format.

To retrieve the third-party token, the library will run the executable using the command specified. The executable's output must adhere to the response format specified in the following examples, and it must output the response to `stdout`.

Here's a sample successful executable OIDC response:
    
    
    {
      "version": 1,
      "success": true,
      "token_type": "urn:ietf:params:oauth:token-type:id_token",
      "id_token": "HEADER.PAYLOAD.SIGNATURE",
      "expiration_time": 1620499962
    }
    

And here's a sample successful executable SAML response:
    
    
    {
      "version": 1,
      "success": true,
      "token_type": "urn:ietf:params:oauth:token-type:saml2",
      "saml_response": "...",
      "expiration_time": 1620499962
    }
    

When you specify an output file using the `--executable-output-file` argument in the credential configuration, successful executable responses must include an `expiration_time` field. This allows the Auth Library to effectively cache and manage the validity of the credentials stored in that file.

Here's a sample executable error response:
    
    
    {
      "version": 1,
      "success": false,
      "code": "401",
      "message": "Caller not authorized."
    }
    

These are all required fields for an error response. The library uses the code and message fields as part of a thrown exception.

Response format fields summary: * **`version`:** The version of the JSON output. Only version 1 is supported. * **`success`:** When true, the response must include the 3rd party token and token type. The response must also include the `expiration_time` field if an output file was specified in the credential configuration. The executable must also exit with an exit code of 0. When false, the response must include the error code and message fields and exit with a non-zero value. * **`token_type`:** This field specifies the 3rd party subject token type. It must be `urn:ietf:params:oauth:token-type:jwt`, `urn:ietf:params:oauth:token-type:id_token`, or `urn:ietf:params:oauth:token-type:saml2`. * **`id_token`:** The 3rd party OIDC token. * **`saml_response`:** The 3rd party SAML response. * **`expiration_time`:** The 3rd party subject token expiration time in seconds (Unix epoch time). * **`code`:** The error code string. * **`message`:** The error message.

All response types must include both the `version` and `success` fields. * Successful responses must include the `token_type` and one of `id_token` or `saml_response`. The `expiration_time` field must also be present if an output file was specified in the credential configuration. * Error responses must include both the `code` and `message` fields.

The library populates the following environment variables when it runs the executable:

  * **`GOOGLE_EXTERNAL_ACCOUNT_AUDIENCE`:** the audience field from the credential configuration. Always present.
  * **`GOOGLE_EXTERNAL_ACCOUNT_TOKEN_TYPE`:** this expected subject token type. Always present.
  * **`GOOGLE_EXTERNAL_ACCOUNT_IMPERSONATED_EMAIL`:** The service account email address. Only present when service account impersonation is used.
  * **`GOOGLE_EXTERNAL_ACCOUNT_OUTPUT_FILE`:** The output file location from the credential configuration. Only present when specified in the credential configuration.



These environment variables can be used by the executable to avoid hard-coding these values.

#### Security considerations

The following security practices are recommended:

  * Prevent rogue processes from running the executable because it will output sensitive credentials to those processes and their users via `stdout`.
  * Prevent rogue processes from altering the configuration or the executable's invocation.



Because of the complexity of using executable-sourced credentials, we strongly recommend that you use other supported mechanisms, such as file or URL sources, for providing third-party credentials unless they don't meet your specific requirements.

You can now use the Auth library to call Google Cloud resources from an OIDC or SAML provider.

### Use a custom supplier with OIDC and SAML

A custom implementation of `IdentityPoolSubjectTokenSupplier` can be used while building `IdentityPoolCredentials` to supply a subject token that can be exchanged for a Google Cloud access token. The supplier must return a valid, unexpired subject token when called by the Google Cloud credential.

`IdentityPoolCredentials` don't cache the returned token, so implement caching logic in the token supplier to prevent multiple requests for the same subject token.
    
    
    import java.io.IOException;
    
    public class CustomTokenSupplier implements IdentityPoolSubjectTokenSupplier {
    
      @Override
      public String getSubjectToken(ExternalAccountSupplierContext context) throws IOException {
        // Any call to the supplier passes a context object with the requested
        // audience and subject token type.
        string audience = context.getAudience();
        string tokenType = context.getSubjectTokenType();
    
        try {
          // Return a valid, unexpired token for the requested audience and token type.
          // Note that IdentityPoolCredentials don't cache the subject token so
          // any caching logic needs to be implemented in the token supplier.
          return retrieveToken(audience, tokenType);
        } catch (Exception e) {
          // If token is unavailable, throw IOException.
          throw new IOException(e);
        }
      }
    
      private String retrieveToken(string tokenType, string audience) {
        // Retrieve a subject token of the requested type for the requested audience.
      }
    }
    
    
    
    CustomTokenSupplier tokenSupplier = new CustomTokenSupplier();
    IdentityPoolCredentials identityPoolCredentials =
        IdentityPoolCredentials.newBuilder()
            .setSubjectTokenSupplier(tokenSupplier) // Sets the token supplier.
            .setAudience(...) // Sets the Google Cloud audience.
            .setSubjectTokenType(SubjectTokenTypes.JWT) // Sets the subject token type.
            .build();
    

Where the [audience](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#provider-audience) is:
    
    
    //iam.googleapis.com/projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>WORKLOAD_POOL_ID</var>/providers/<var>PROVIDER_ID</var>
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`WORKLOAD_POOL_ID`:** the workload identity pool ID.
  * **`PROVIDER_ID`:** the provider ID.



You can also find the values for audience, service account impersonation URL, and any other builder field by generating a [credential configuration file with the gcloud CLI](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config).

### Use a custom supplier with AWS

A custom implementation of `AwsSecurityCredentialsSupplier` can be provided when initializing `AwsCredentials`. If provided, the `AwsCredentials` instance will defer to the supplier to retrieve AWS security credentials to exchange for a Google Cloud access token. The supplier must return valid, unexpired AWS security credentials when called by the Google Cloud credential.

`AwsCredentials` don't cache the returned AWS security credentials or region, so implement caching logic in the supplier to prevent multiple requests for the same resources.
    
    
    class CustomAwsSupplier implements AwsSecurityCredentialsSupplier {
      @Override
      AwsSecurityCredentials getAwsSecurityCredentials(ExternalAccountSupplierContext context) throws IOException {
        // Any call to the supplier passes a context object with the requested
        // audience.
        String audience = context.getAudience();
    
        try {
          // Return valid, unexpired AWS security credentials for the requested audience.
          // Note that AwsCredentials don't cache the AWS security credentials so
          // any caching logic needs to be implemented in the credentials' supplier.
          return retrieveAwsSecurityCredentials(audience);
        } catch (Exception e) {
          // If credentials are unavailable, throw IOException.
          throw new IOException(e);
        }
      }
    
      @Override
      String getRegion(ExternalAccountSupplierContext context) throws IOException {
        try {
          // Return a valid AWS region. i.e. "us-east-2".
          // Note that AwsCredentials don't cache the region so
          // any caching logic needs to be implemented in the credentials' supplier.
          return retrieveAwsRegion();
        } catch (Exception e) {
          // If region is unavailable, throw IOException.
          throw new IOException(e);
        }
      }
    
      private AwsSecurityCredentials retrieveAwsSecurityCredentials(string audience) {
        // Retrieve Aws security credentials for the requested audience.
      }
    
      private String retrieveAwsRegion() {
        // Retrieve current AWS region.
      }
    }
    
    
    
    CustomAwsSupplier awsSupplier = new CustomAwsSupplier();
    AwsCredentials credentials = AwsCredentials.newBuilder()
        .setSubjectTokenType(SubjectTokenTypes.AWS4) // Sets the subject token type.
        .setAudience(...) // Sets the Google Cloud audience.
        .setAwsSecurityCredentialsSupplier(supplier) // Sets the supplier.
        .build();
    

Where the [audience](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#provider-audience) is: `//iam.googleapis.com/projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>WORKLOAD_POOL_ID</var>/providers/<var>PROVIDER_ID</var>`

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`WORKLOAD_POOL_ID`:** the workload identity pool ID.
  * **`PROVIDER_ID`:** the provider ID.



You can also find the values for audience, service account impersonation URL, and any other builder field by generating a [credential configuration file with the gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config).

### Configurable token lifetime

When you create a credential configuration with workload identity federation using service account impersonation, you can provide an optional argument to configure the service account access token lifetime.

To generate the configuration with configurable token lifetime, run the following command (this example uses an AWS configuration, but the token lifetime can be configured for all workload identity federation providers):
    
    
      # Generate an AWS configuration file with configurable token lifetime.
      gcloud iam workload-identity-pools create-cred-config \
          projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>POOL_ID</var>/providers/<var>AWS_PROVIDER_ID</var> \
          --service-account <var>SERVICE_ACCOUNT_EMAIL</var> \
          --aws \
          --output-file /path/to/generated/config.json \
          --service-account-token-lifetime-seconds <var>TOKEN_LIFETIME</var>
    

Replace the following:

  * **`PROJECT_NUMBER`:** the Google Cloud project number.
  * **`POOL_ID`:** the workload identity pool ID.
  * **`AWS_PROVIDER_ID`:** the AWS provider ID.
  * **`SERVICE_ACCOUNT_EMAIL`:** the email of the service account to impersonate.
  * **`TOKEN_LIFETIME`:** the selected lifetime duration of the service account access token in seconds.



The `service-account-token-lifetime-seconds` flag is optional. If not provided, the flag defaults to one hour. The minimum allowed value is 600 (10 minutes) and the maximum allowed value is 43200 (12 hours). If you require a lifetime greater than one hour, you must add the service account as an allowed value in an Organization Policy Service that enforces the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` constraint.

Configuring a short lifetime (for example, 10 minutes) causes the library to initiate the entire token exchange flow every 10 minutes. This calls the 3rd party token provider even if the 3rd party token is not expired.

### Use external account authorized user workforce credentials

[External account authorized user credentials](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#browser-based-sign-in) let you to sign in with a web browser to an external identity provider account using the gcloud CLI and create a configuration for the auth library to use.

To generate an external account authorized user workforce identity configuration, run the following command:
    
    
    gcloud auth application-default login --login-config=LOGIN_CONFIG
    

Where the following variable needs to be substituted:

  * **`LOGIN_CONFIG`:** the login config file generated with Google Cloud console or [gcloud iam workforce-pools create-login-config](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config)



This opens a browser flow for you to sign in using the configured third-party identity provider. It then stores the external account authorized user configuration at the well-known ADC location.

The Auth library will then use the provided refresh token from the configuration to generate and refresh an access token to call Google Cloud services.

The default lifetime of the refresh token is one hour. After this, you need to generate a new configuration from the gcloud CLI. You can modify the lifetime by changing the [session duration of the workforce pool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools), and you can set it as high as 12 hours.

### Use external identities

You can use external identities with `Application Default Credentials`. To use external identities with Application Default Credentials, generate the JSON credentials configuration file for your external identity as described in the Workload Identity Federation section. Once generated, store the path to this file in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/config.json
    

The library can now choose the right type of client and initialize credentials from the context that the configuration file provides.
    
    
    GoogleCredentials googleCredentials = GoogleCredentials.getApplicationDefault();
    
    String projectId = "your-project-id";
    String url = "https://storage.googleapis.com/storage/v1/b?project=" + projectId;
    
    HttpCredentialsAdapter credentialsAdapter = new HttpCredentialsAdapter(googleCredentials);
    HttpRequestFactory requestFactory = new NetHttpTransport().createRequestFactory(credentialsAdapter);
    HttpRequest request = requestFactory.buildGetRequest(new GenericUrl(url));
    
    JsonObjectParser parser = new JsonObjectParser(GsonFactory.getDefaultInstance());
    request.setParser(parser);
    
    HttpResponse response = request.execute();
    System.out.println(response.parseAsString());
    

You can also explicitly initialize external account clients using the generated configuration file.
    
    
    ExternalAccountCredentials credentials =
        ExternalAccountCredentials.fromStream(new FileInputStream("/path/to/credentials.json"));
    

#### Security considerations

This library does not perform any validation on the `token_url`, `token_info_url`, or `service_account_impersonation_url` fields of the credential configuration. We don't recommend that you use a credential configuration that you did not generate with the gcloud CLI unless you verify that the URL fields point to a googleapis.com domain.

### Downscope with Credential Access Boundaries

[Downscoping with Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials) enables restricting the Identity and Access Management (IAM) permissions that a short-lived credential can use for Cloud Storage. This involves creating a `CredentialAccessBoundary` that defines the restrictions that apply to the downscoped token. Using downscoped credentials ensures that tokens in flight always have the least privileges. See [Principle of Least Privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).

#### Create a `CredentialAccessBoundary`

The Credential Access Boundary specifies which resources the newly created credential can access. It also specifies an upper bound on the permissions that are available on each resource. It includes one or more `AccessBoundaryRule` objects.

The following snippet shows how to initialize a `CredentialAccessBoundary` with one `AccessBoundaryRule`. This rule specifies that the downscoped token will have read-only access to objects starting with `customer-a` in bucket `bucket-123`.
    
    
    // Create the AccessBoundaryRule.
    String availableResource = "//storage.googleapis.com/projects/_/buckets/bucket-123";
    String availablePermission = "inRole:roles/storage.objectViewer";
    String expression =  "resource.name.startsWith('projects/_/buckets/bucket-123/objects/customer-a')";
    
    CredentialAccessBoundary.AccessBoundaryRule rule =
        CredentialAccessBoundary.AccessBoundaryRule.newBuilder()
            .setAvailableResource(availableResource)
            .addAvailablePermission(availablePermission)
            .setAvailabilityCondition(
            CredentialAccessBoundary.AccessBoundaryRule.AvailabilityCondition.newBuilder().setExpression(expression).build())
            .build();
    
    // Create the CredentialAccessBoundary with the rule.
    CredentialAccessBoundary credentialAccessBoundary =
            CredentialAccessBoundary.newBuilder().addRule(rule).build();
    

#### Common usage pattern

The common usage pattern involves a token broker with elevated access. This broker generates downscoped credentials from higher access source credentials. It then passes the downscoped short-lived access tokens to a token consumer through a secure authenticated channel for limited access to Google Cloud Storage resources.

#### Generate downscoped tokens

There are two ways to generate downscoped tokens using a `CredentialAccessBoundary`:

  * **Server-side (using`DownscopedCredentials`):** the client calls the Security Token Service (STS) each time a downscoped token is needed. This is suitable for applications where Credential Access Boundary rules change infrequently or where you reuse a single downscoped credential many times. A key consideration is that every rule change requires you to make a new call to the STS. This approach is available within the `google-auth-library-oauth2-http` library and does not require any additional dependencies. This makes it simpler to integrate. It is a good choice if your use case doesn't demand the specific benefits of the client-side approach.

  * **Client-side (using`ClientSideCredentialAccessBoundaryFactory`):** the client retrieves cryptographic material once and then generates multiple downscoped tokens locally. This minimizes calls to the STS and is more efficient when Credential Access Boundary rules change frequently, because the client doesn't need to contact the STS for each rule change. This is also more efficient for applications that need to generate many unique downscoped tokens. This approach is available in the `google-auth-library-cab-token-generator` module. However, this module comes with its own set of dependencies. These dependencies can add complexity to your project. Consider this approach if minimizing STS calls and generating numerous unique tokens are primary concerns. You will also need to manage the additional dependencies.




#### Server-side CAB

The `DownscopedCredentials` class can be used to produce a downscoped access token from a source credential and the `CredentialAccessBoundary`.
    
    
    // Retrieve the source credentials from ADC.
    GoogleCredentials sourceCredentials = GoogleCredentials.getApplicationDefault()
            .createScoped("https://www.googleapis.com/auth/cloud-platform");
    
    // Create an Access Boundary Rule which will restrict the downscoped token to having read-only
    // access to objects starting with "customer-a" in bucket "bucket-123".
    String availableResource = "//storage.googleapis.com/projects/_/buckets/bucket-123";
    String availablePermission = "inRole:roles/storage.objectViewer";
    String expression =  "resource.name.startsWith('projects/_/buckets/bucket-123/objects/customer-a')";
    
    CredentialAccessBoundary.AccessBoundaryRule rule =
        CredentialAccessBoundary.AccessBoundaryRule.newBuilder()
            .setAvailableResource(availableResource)
            .addAvailablePermission(availablePermission)
            .setAvailabilityCondition(
                new AvailabilityCondition(expression, /* title= */ null, /* description= */ null))
            .build();
    
    // Initialize the DownscopedCredentials class.
    DownscopedCredentials downscopedCredentials =
        DownscopedCredentials.newBuilder()
            .setSourceCredential(sourceCredentials)
            .setCredentialAccessBoundary(CredentialAccessBoundary.newBuilder().addRule(rule).build())
            .build();
    
    // Retrieve the downscoped access token.
    // You will need to pass this to the Token Consumer.
    AccessToken downscopedAccessToken = downscopedCredentials.refreshAccessToken();
    

#### Client-side CAB

For client-side CAB, the `ClientSideCredentialAccessBoundaryFactory` is used with a source credential. After initializing the factory, the `generateToken()` method can be called repeatedly with different `CredentialAccessBoundary` objects to create multiple downscoped tokens.
    
    
    // Retrieve the source credentials from ADC.
    GoogleCredentials sourceCredentials = GoogleCredentials.getApplicationDefault()
            .createScoped("https://www.googleapis.com/auth/cloud-platform");
    
    // Create an Access Boundary Rule which will restrict the downscoped token to having read-only
    // access to objects starting with "customer-a" in bucket "bucket-123".
    String availableResource = "//storage.googleapis.com/projects/_/buckets/bucket-123";
    String availablePermission = "inRole:roles/storage.objectViewer";
    String expression =  "resource.name.startsWith('projects/_/buckets/bucket-123/objects/customer-a')";
    
    CredentialAccessBoundary.AccessBoundaryRule rule =
        CredentialAccessBoundary.AccessBoundaryRule.newBuilder()
            .setAvailableResource(availableResource)
            .addAvailablePermission(availablePermission)
            .setAvailabilityCondition(
                new AvailabilityCondition(expression, /* title= */ null, /* description= */ null))
            .build();
    
    // Initialize the ClientSideCredentialAccessBoundaryFactory.
    ClientSideCredentialAccessBoundaryFactory factory =
        ClientSideCredentialAccessBoundaryFactory.newBuilder()
            .setSourceCredential(sourceCredentials)
            .build();
    
    // Create the CredentialAccessBoundary with the rule.
    CredentialAccessBoundary credentialAccessBoundary =
            CredentialAccessBoundary.newBuilder().addRule(rule).build();
    
    // Generate the downscoped access token.
    // You will need to pass this to the Token Consumer.
    AccessToken downscopedAccessToken = factory.generateToken(credentialAccessBoundary);
    

#### Use downscoped access tokens

You can set up a token broker on a server in a private network. Various workloads (token consumers) in the same network send authenticated requests to that broker for downscoped tokens. These tokens allow them to access or modify specific Google Cloud Storage buckets.

The broker instantiates downscoped credentials instances that can generate short-lived downscoped access tokens. It then passes these tokens to the token consumer.

These downscoped access tokens can be used by the Token Consumer using `OAuth2Credentials` or `OAuth2CredentialsWithRefresh`. You can then use this credential to initialize a storage client instance to access Google Cloud Storage resources with restricted access.
    
    
    // You can pass an `OAuth2RefreshHandler` to `OAuth2CredentialsWithRefresh` that will allow the
    // library to seamlessly handle downscoped token refreshes on expiration.
    OAuth2CredentialsWithRefresh.OAuth2RefreshHandler handler =
            new OAuth2CredentialsWithRefresh.OAuth2RefreshHandler() {
        @Override
        public AccessToken refreshAccessToken() {
          // Retrieve the token from your Token Broker.
          return accessToken;
        }
    };
    
    // The downscoped token is retrieved from the token broker.
    AccessToken downscopedToken = handler.refreshAccessToken();
    
    // Build the OAuth2CredentialsWithRefresh from the downscoped token and pass a refresh handler
    // to handle token expiration. Passing the original downscoped token or the expiry here is optional,
    // because the refresh_handler will generate the downscoped token on demand.
    OAuth2CredentialsWithRefresh credentials =
        OAuth2CredentialsWithRefresh.newBuilder()
            .setAccessToken(downscopedToken)
            .setRefreshHandler(handler)
            .build();
    
    // Use the credentials with the Cloud Storage SDK.
    StorageOptions options = StorageOptions.newBuilder().setCredentials(credentials).build();
    Storage storage = options.getService();
    
    // Call Cloud Storage APIs.
    // Because we passed the downscoped credential, we will have limited read-only access to objects
    // starting with "customer-a" in bucket "bucket-123".
    storage.get(...)
    

Only Cloud Storage supports Credential Access Boundaries; other Google Cloud services don't support this feature.

## Use credentials with `google-http-client`

Credentials provided by [com.google.auth:google-auth-library-oauth2-http](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http) can be used with Google's HTTP-based clients. Google's HTTP-based clients provide an `HttpCredentialsAdapter` which can be used as an `HttpRequestInitializer`, the last argument for their builders.
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.services.bigquery.Bigquery;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    
    [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)();
    [HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html) requestInitializer = new [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html)(credentials);
    
    Bigquery bq = new Bigquery.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
        .setApplicationName(APPLICATION_NAME)
        .build();
    

## Verify JWT Tokens (Beta feature)

To verify a JWT token, use the `TokenVerifier` class.

### Verify a signature

To verify a signature, use the default `TokenVerifier`:
    
    
    import com.google.api.client.json.webtoken.[JsonWebSignature](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebSignature.html);
    import com.google.auth.oauth2.[TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html);
    
    [TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html) tokenVerifier = [TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html).newBuilder().build();
    try {
      [JsonWebSignature](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebSignature.html) jsonWebSignature = tokenVerifier.[verify](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html#com_google_auth_oauth2_TokenVerifier_verify_java_lang_String_)(tokenString);
      // Optionally, verify additional claims.
      if (!"expected-value".equals(jsonWebSignature.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.html#com_google_api_client_json_webtoken_JsonWebToken_getPayload__)().get("additional-claim"))) {
        // Handle custom verification error.
      }
    } catch ([TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html).[VerificationException](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.VerificationException.html) e) {
      // The token is invalid.
    }
    

### Customize the `TokenVerifier`

To customize a `TokenVerifier`, instantiate it using its builder:
    
    
    import com.google.api.client.json.webtoken.[JsonWebSignature](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebSignature.html);
    import com.google.auth.oauth2.[TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html);
    
    [TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html) tokenVerifier = [TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html).newBuilder()
      .setAudience("audience-to-verify")
      .setIssuer("issuer-to-verify")
      .build();
    try {
      [JsonWebSignature](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebSignature.html) jsonWebSignature = tokenVerifier.[verify](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html#com_google_auth_oauth2_TokenVerifier_verify_java_lang_String_)(tokenString);
      // Optionally, verify additional claims.
      if (!"expected-value".equals(jsonWebSignature.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.html#com_google_api_client_json_webtoken_JsonWebToken_getPayload__)().get("additional-claim"))) {
        // Handle custom verification error.
      }
    } catch ([TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html).[VerificationException](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.VerificationException.html) e) {
      // The token is invalid.
    }
    

For more options, see the [`TokenVerifier.Builder`](https://cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.Builder) documentation.

## `google-auth-library-credentials`

This artifact contains base classes and interfaces for Google credentials:

  * **`Credentials`:** this is the base class for an authorized identity. Implementations of this class can authorize your application.
  * **`RequestMetadataCallback`:** this is the interface for the callback that receives the result of the asynchronous `Credentials.getRequestMetadata(URI, Executor, RequestMetadataCallback)`.
  * **`ServiceAccountSigner`:** this is the interface for a service account signer. Implementations of this class are capable of signing byte arrays using the credentials associated to a Google Service Account.



## `google-auth-library-appengine`

This artifact depends on the App Engine SDK (`appengine-api-1.0-sdk`). Use it only for applications running on App Engine environments that use `urlfetch`. The `AppEngineCredentials` class lets you authorize your App Engine application given an instance of [AppIdentityService](https://docs.cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/appidentity/AppIdentityService).

Usage:
    
    
    import com.google.appengine.api.appidentity.[AppIdentityService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.html);
    import com.google.appengine.api.appidentity.[AppIdentityServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServiceFactory.html);
    import com.google.auth.[Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials.html);
    import com.google.auth.appengine.[AppEngineCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.appengine.AppEngineCredentials.html);
    
    [AppIdentityService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.html) appIdentityService = [AppIdentityServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServiceFactory.html).getAppIdentityService();
    
    [Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials.html) credentials =
        [AppEngineCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.appengine.AppEngineCredentials.html).newBuilder()
            .setScopes(...)
            .setAppIdentityService(appIdentityService)
            .build();
    

**Important:** `com.google.auth.appengine.AppEngineCredentials` is a separate class from `com.google.auth.oauth2.AppEngineCredentials`.

## google-auth-library-cab-token-generator

This module provides the `ClientSideCredentialAccessBoundaryFactory` class, enabling client-side generation of downscoped tokens for Cloud Storage using Credential Access Boundaries. This approach is particularly useful for applications requiring frequent changes to Credential Access Boundary rules or the generation of many unique downscoped tokens, because it minimizes calls to the Security Token Service (STS). For usage examples, see the Client-side CAB section. This module comes with its own set of dependencies. Evaluate whether the benefits of client-side downscoping outweigh the added complexity for your specific use case.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
