---
url: https://docs.cloud.google.com/iam/docs/authenticate-with-auth-libraries/
title: Authenticate workloads with Google Cloud auth libraries \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:09.530214+00:00
---

# Authenticate workloads with Google Cloud auth libraries  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/authenticate-with-auth-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Authenticate workloads with Google Cloud auth libraries Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) with Google Cloud authentication libraries, known as auth libraries, to authenticate workloads from third-party identity providers such as AWS, Microsoft Azure, and providers that support OpenID Connect (OIDC) or SAML 2.0.

Workload Identity Federation lets applications running outside Google Cloud access Google Cloud resources without using service account keys. The Google auth libraries enable this by exchanging external credentials for short-lived Google Cloud access tokens.

For authentication, you can obtain external credentials using the following methods:

  * Standard mechanism for common setups.
  * Custom credential suppliers for complex workflows that require you to write your own code.



## Before you begin

  1. Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,sts.googleapis.com,iamcredentials.googleapis.com)

  2. Configure Workload Identity Federation with your identity provider.

     * [AWS or Azure VMs](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds)
     * [OIDC or SAML](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers)



## Authenticate using the standard credential mechanism

For commonly supported third-party identity providers, you can use the Google Cloud auth library's built-in capabilities to authenticate your workloads by generating a credential configuration file. This file provides the necessary information for the auth libraries to federate identities from external providers.

The credential configuration file, typically loaded using the `GOOGLE_APPLICATION_CREDENTIALS` environment variable, can instruct the auth libraries to obtain the third-party subject token using one of the following methods:

  * **File-sourced:** The library reads the subject token from a local file. A separate process must ensure this file contains a valid, unexpired token.
  * **URL-sourced:** The library fetches the subject token by making a request to a specified local URL endpoint.
  * **Executable-sourced:** The library runs a configured executable command. The standard output of the executable is expected to contain the subject token.


  1. Generate the credential configuration file for your specific provider:

     * [AWS](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#create-cred-config)
     * [Azure](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#create-cred-config)
     * [OIDC or SAML identity provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#create-credential-config)

This page includes instructions for the following:

       * [File-sourced credentials](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#file-sourced-credentials)
       * [URL-sourced credentials](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#url-sourced-credentials)
       * [Executable-sourced credentials](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#executable-sourced-credentials)
  2. Use the credential configuration file to authenticate.

To let the Google Cloud client libraries automatically locate and use your credential configuration file, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the generated JSON file.

Export the environment variable in your shell: `bash export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/config.json`

After you set the environment variable, the client libraries handle the authentication flow.




The following code sample shows how to make an authenticated call to a Google Cloud API:

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://googleapis.dev/nodejs/googleapis/latest/iam/index.html). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library.
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Instantiates a client. If you don't specify credentials when constructing
    // the client, the client library will look for credentials in the
    // environment.
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    // Makes an authenticated API request.
    async function listBuckets() {
      try {
        const results = await storage.[getBuckets](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)();
    
        const [buckets] = results;
    
        console.log('Buckets:');
        buckets.forEach(bucket => {
          console.log(bucket.name);
        });
      } catch (err) {
        console.error('ERROR:', err);
      }
    }
    listBuckets();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def implicit():
        from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
        # If you don't specify credentials when constructing the client, the
        # client library will look for credentials in the environment.
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        # Make an authenticated API request
        buckets = list(storage_client.[list_buckets](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_buckets)())
        print(buckets)
    
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void authImplicit() {
      // If you don't specify credentials when constructing the client, the client library will
      // look for credentials via the environment variable GOOGLE_APPLICATION_CREDENTIALS.
      Storage storage = StorageOptions.getDefaultInstance().getService();
    
      System.out.println("Buckets:");
      Page<Bucket> buckets = storage.list();
      for (Bucket bucket : buckets.iterateAll()) {
        System.out.println(bucket.toString());
      }
    }

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/storage"
    	"google.golang.org/api/iterator"
    )
    
    // authenticateImplicitWithAdc uses Application Default Credentials
    // to automatically find credentials and authenticate.
    func authenticateImplicitWithAdc(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectId string) error {
    	// projectId := "your_project_id"
    
    	ctx := context.Background()
    
    	// NOTE: Replace the client created below with the client required for your application.
    	// Note that the credentials are not specified when constructing the client.
    	// The client library finds your credentials using ADC.
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	it := client.[Buckets](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Buckets)(ctx, projectId)
    	for {
    		bucketAttrs, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "Bucket: %v\n", bucketAttrs.Name)
    	}
    
    	fmt.Fprintf(w, "Listed all storage buckets.\n")
    
    	return nil
    }
    

**Note:** Workload Identity Federation is also supported in C++, C#, Go, Java, Node.js, PHP, Python, Ruby, and Objective-C.

## Authenticate using custom credential suppliers

If your environment doesn't support the built-in capabilities of the Google auth library or if you want to implement custom logic to supply credentials to the Google auth library, use custom credential suppliers to authenticate your workloads.

### Access resources from AWS

When you initialize the authentication client, provide a custom implementation of a credential supplier. The client instance defers to the supplier to retrieve AWS security credentials to exchange for a Google Cloud access token. The supplier must return valid and unexpired credentials when the client calls it.

The authentication client doesn't cache the returned AWS security credentials or region, so implement caching in the supplier to prevent redundant requests for the same resources.

The following code samples show how you can set up access to Google Cloud resources from AWS with a custom credential supplier.

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://googleapis.dev/nodejs/googleapis/latest/iam/index.html). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {AwsClient} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    const {fromNodeProviderChain} = require('@aws-sdk/credential-providers');
    const fs = require('fs');
    const path = require('path');
    const {STSClient} = require('@aws-sdk/client-sts');
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    /**
     * Custom AWS Security Credentials Supplier.
     *
     * This implementation resolves AWS credentials using the default Node provider
     * chain from the AWS SDK. This allows fetching credentials from environment
     * variables, shared credential files (~/.aws/credentials), or IAM roles
     * for service accounts (IRSA) in EKS, etc.
     */
    class CustomAwsSupplier {
      constructor() {
        this.region = null;
    
        this.awsCredentialsProvider = fromNodeProviderChain();
      }
    
      /**
       * Returns the AWS region. This is required for signing the AWS request.
       * It resolves the region automatically by using the default AWS region
       * provider chain, which searches for the region in the standard locations
       * (environment variables, AWS config file, etc.).
       */
      async getAwsRegion(_context) {
        if (this.region) {
          return this.region;
        }
    
        const client = new STSClient({});
        this.region = await client.config.region();
    
        if (!this.region) {
          throw new Error(
            'CustomAwsSupplier: Unable to resolve AWS region. Please set the AWS_REGION environment variable or configure it in your ~/.aws/config file.'
          );
        }
    
        return this.region;
      }
    
      /**
       * Retrieves AWS security credentials using the AWS SDK's default provider chain.
       */
      async getAwsSecurityCredentials(_context) {
        const awsCredentials = await this.awsCredentialsProvider();
    
        if (!awsCredentials.accessKeyId || !awsCredentials.secretAccessKey) {
          throw new Error(
            'Unable to resolve AWS credentials from the node provider chain. ' +
              'Ensure your AWS CLI is configured, or AWS environment variables (like AWS_ACCESS_KEY_ID) are set.'
          );
        }
    
        return {
          accessKeyId: awsCredentials.accessKeyId,
          secretAccessKey: awsCredentials.secretAccessKey,
          token: awsCredentials.sessionToken,
        };
      }
    }
    
    /**
     * Authenticates with Google Cloud using AWS credentials and retrieves bucket metadata.
     *
     * @param {string} bucketName The name of the bucket to retrieve.
     * @param {string} audience The Workload Identity Pool audience.
     * @param {string} [impersonationUrl] Optional Service Account impersonation URL.
     */
    async function authenticateWithAwsCredentials(
      bucketName,
      audience,
      impersonationUrl
    ) {
      const customSupplier = new CustomAwsSupplier();
    
      const clientOptions = {
        audience: audience,
        subject_token_type: 'urn:ietf:params:aws:token-type:aws4_request',
        service_account_impersonation_url: impersonationUrl,
        aws_security_credentials_supplier: customSupplier,
      };
    
      const authClient = new [AwsClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/awsclient.html)(clientOptions);
    
      const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)({
        authClient: authClient,
      });
    
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      return metadata;
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    import os
    import sys
    
    import boto3
    from google.auth import aws
    from google.auth import [exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html)
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    class CustomAwsSupplier(aws.AwsSecurityCredentialsSupplier):
        """Custom AWS Security Credentials Supplier using Boto3."""
    
        def __init__(self):
            """Initializes the Boto3 session, prioritizing environment variables for region."""
            # Explicitly read the region from the environment first.
            region = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION")
    
            # If region is None, Boto3's discovery chain will be used when needed.
            self.session = boto3.Session(region_name=region)
            self._cached_region = None
    
        def get_aws_region(self, context, request) -> str:
            """Returns the AWS region using Boto3's default provider chain."""
            if self._cached_region:
                return self._cached_region
    
            self._cached_region = self.session.region_name
    
            if not self._cached_region:
                raise [exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).GoogleAuthError(
                    "Boto3 was unable to resolve an AWS region."
                )
    
            return self._cached_region
    
        def get_aws_security_credentials(
            self, context, request=None
        ) -> aws.AwsSecurityCredentials:
            """Retrieves AWS security credentials using Boto3's default provider chain."""
            creds = self.session.get_credentials()
            if not creds:
                raise [exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).GoogleAuthError(
                    "Unable to resolve AWS credentials from Boto3."
                )
    
            return aws.AwsSecurityCredentials(
                access_key_id=creds.access_key,
                secret_access_key=creds.secret_key,
                session_token=creds.token,
            )
    
    
    def authenticate_with_aws_credentials(bucket_name, audience, impersonation_url=None):
        """Authenticates using the custom AWS supplier and gets bucket metadata.
    
        Returns:
            dict: The bucket metadata response from the Google Cloud Storage API.
        """
    
        custom_supplier = CustomAwsSupplier()
    
        credentials = aws.Credentials(
            audience=audience,
            subject_token_type="urn:ietf:params:aws:token-type:aws4_request",
            service_account_impersonation_url=impersonation_url,
            aws_security_credentials_supplier=custom_supplier,
            scopes=["https://www.googleapis.com/auth/devstorage.read_only"],
        )
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(credentials=credentials)
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        return bucket._properties
    
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.auth.oauth2.[AwsCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsCredentials.html);
    import com.google.auth.oauth2.[AwsSecurityCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsSecurityCredentials.html);
    import com.google.auth.oauth2.[AwsSecurityCredentialsSupplier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsSecurityCredentialsSupplier.html);
    import com.google.auth.oauth2.[ExternalAccountSupplierContext](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ExternalAccountSupplierContext.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.gson.Gson;
    import com.google.gson.reflect.TypeToken;
    import java.io.IOException;
    import java.io.Reader;
    import java.lang.reflect.Type;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.Map;
    import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
    import software.amazon.awssdk.auth.credentials.AwsSessionCredentials;
    import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
    import software.amazon.awssdk.regions.Region;
    import software.amazon.awssdk.regions.providers.DefaultAwsRegionProviderChain;
    
      public static [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) authenticateWithAwsCredentials(
          String gcpWorkloadAudience, String saImpersonationUrl, String gcsBucketName)
          throws IOException {
    
        CustomAwsSupplier customSupplier = new CustomAwsSupplier();
    
        [AwsCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsCredentials.html).Builder credentialsBuilder =
            [AwsCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsCredentials.html).newBuilder()
                .setAudience(gcpWorkloadAudience)
                // This token type indicates that the subject token is an AWS Signature Version 4 signed
                // request. This is required for AWS Workload Identity Federation.
                .setSubjectTokenType("urn:ietf:params:aws:token-type:aws4_request")
                .[setAwsSecurityCredentialsSupplier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsCredentials.Builder.html#com_google_auth_oauth2_AwsCredentials_Builder_setAwsSecurityCredentialsSupplier_com_google_auth_oauth2_AwsSecurityCredentialsSupplier_)(customSupplier);
    
        if (saImpersonationUrl != null) {
          credentialsBuilder.setServiceAccountImpersonationUrl(saImpersonationUrl);
        }
    
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = credentialsBuilder.build();
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setCredentials(credentials).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        return storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(gcsBucketName);
      }
    
      /**
       * Custom AWS Security Credentials Supplier.
       *
       * <p>This implementation resolves AWS credentials and regions using the default provider chains
       * from the AWS SDK (v2). This supports environment variables, ~/.aws/credentials, and EC2/EKS
       * metadata.
       */
      private static class CustomAwsSupplier implements [AwsSecurityCredentialsSupplier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsSecurityCredentialsSupplier.html) {
        private final AwsCredentialsProvider awsCredentialsProvider;
        private String region;
    
        public CustomAwsSupplier() {
          // The AWS SDK handles caching internally.
          this.awsCredentialsProvider = DefaultCredentialsProvider.create();
        }
    
        @Override
        public String getRegion([ExternalAccountSupplierContext](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ExternalAccountSupplierContext.html) context) {
          if (this.region == null) {
            Region awsRegion = new DefaultAwsRegionProviderChain().[getRegion](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsSecurityCredentialsSupplier.html#com_google_auth_oauth2_AwsSecurityCredentialsSupplier_getRegion_com_google_auth_oauth2_ExternalAccountSupplierContext_)();
            if (awsRegion == null) {
              throw new IllegalStateException(
                  "Unable to resolve AWS region. Ensure AWS_REGION is set or configured.");
            }
            this.region = awsRegion.id();
          }
          return this.region;
        }
    
        @Override
        public [AwsSecurityCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsSecurityCredentials.html) getCredentials([ExternalAccountSupplierContext](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ExternalAccountSupplierContext.html) context) {
          software.amazon.awssdk.auth.credentials.[AwsCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsCredentials.html) credentials =
              this.awsCredentialsProvider.resolveCredentials();
    
          if (credentials == null) {
            throw new IllegalStateException("Unable to resolve AWS credentials.");
          }
    
          String sessionToken = null;
          if (credentials instanceof AwsSessionCredentials) {
            sessionToken = ((AwsSessionCredentials) credentials).sessionToken();
          }
    
          return new [AwsSecurityCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AwsSecurityCredentials.html)(
              credentials.accessKeyId(), credentials.secretAccessKey(), sessionToken);
        }
      }

### Access resources from OIDC and SAML

When you initialize the authentication client, provide a custom token supplier to provide a subject token that is exchanged for a Google Cloud access token. The supplier must return a valid and unexpired subject token when the client calls it.

The authentication client doesn't cache the returned token, so implement caching in the supplier to prevent redundant requests for the same subject token.

The following code samples show how you can set up access to Google Cloud resources from providers that support OpenID Connect (OIDC) or SAML 2.0 with a custom credential supplier.

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://googleapis.dev/nodejs/googleapis/latest/iam/index.html). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {IdentityPoolClient} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    const {Gaxios} = require('[gaxios](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html)');
    const fs = require('fs');
    const path = require('path');
    
    /**
     * A custom SubjectTokenSupplier that authenticates with Okta using the
     * Client Credentials grant flow.
     */
    class OktaClientCredentialsSupplier {
      constructor(domain, clientId, clientSecret) {
        const cleanDomain = domain.endsWith('/') ? domain.slice(0, -1) : domain;
        this.oktaTokenUrl = `${cleanDomain}/oauth2/default/v1/token`;
    
        this.clientId = clientId;
        this.clientSecret = clientSecret;
        this.accessToken = null;
        this.expiryTime = 0;
        this.[gaxios](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html) = new [Gaxios](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxios.html)();
      }
    
      /**
       * Main method called by the auth library. It will fetch a new token if one
       * is not already cached.
       * @returns {Promise<string>} A promise that resolves with the Okta Access token.
       */
      async getSubjectToken() {
        const isTokenValid =
          this.accessToken && Date.now() < this.expiryTime - 60 * 1000;
    
        if (isTokenValid) {
          return this.accessToken;
        }
    
        const {accessToken, expiresIn} = await this.fetchOktaAccessToken();
        this.accessToken = accessToken;
        this.expiryTime = Date.now() + expiresIn * 1000;
        return this.accessToken;
      }
    
      /**
       * Performs the Client Credentials grant flow with Okta.
       */
      async fetchOktaAccessToken() {
        const params = new URLSearchParams();
        [params](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxiosoptions.html).append('grant_type', 'client_credentials');
        [params](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxiosoptions.html).append('scope', 'gcp.test.read');
    
        const authHeader =
          'Basic ' +
          Buffer.from(`${this.clientId}:${this.clientSecret}`).toString('[base64](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/policydocument.html)');
    
        try {
          const response = await this.[gaxios](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html).[request](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html)({
            url: this.oktaTokenUrl,
            method: 'POST',
            headers: {
              Authorization: authHeader,
              'Content-Type': 'application/x-www-form-urlencoded',
            },
            data: [params](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxiosoptions.html).toString(),
          });
    
          const {access_token, expires_in} = response.data;
          if (access_token && expires_in) {
            return {accessToken: access_token, expiresIn: expires_in};
          } else {
            throw new Error(
              'Access token or expires_in not found in Okta response.'
            );
          }
        } catch (error) {
          throw new Error(
            `Failed to authenticate with Okta: ${error.response?.data || error.message}`
          );
        }
      }
    }
    
    /**
     * Authenticates with Google Cloud using Okta credentials and retrieves bucket metadata.
     *
     * @param {string} bucketName The name of the bucket to retrieve.
     * @param {string} audience The Workload Identity Pool audience.
     * @param {string} domain The Okta domain.
     * @param {string} clientId The Okta client ID.
     * @param {string} clientSecret The Okta client secret.
     * @param {string} [impersonationUrl] Optional Service Account impersonation URL.
     */
    async function authenticateWithOktaCredentials(
      bucketName,
      audience,
      domain,
      clientId,
      clientSecret,
      impersonationUrl
    ) {
      const oktaSupplier = new OktaClientCredentialsSupplier(
        domain,
        clientId,
        clientSecret
      );
    
      const authClient = new [IdentityPoolClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/identitypoolclient.html)({
        audience: audience,
        subject_token_type: 'urn:ietf:params:oauth:token-type:jwt',
        token_url: 'https://sts.googleapis.com/v1/token',
        subject_token_supplier: oktaSupplier,
        service_account_impersonation_url: impersonationUrl,
      });
    
      const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)({
        authClient: authClient,
      });
    
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      return metadata;
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    import time
    import urllib.parse
    
    from google.auth import identity_pool
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import requests
    
    
    class OktaClientCredentialsSupplier:
        """A custom SubjectTokenSupplier that authenticates with Okta.
    
        This supplier uses the Client Credentials grant flow for machine-to-machine
        (M2M) authentication with Okta.
        """
    
        def __init__(self, domain, client_id, client_secret):
            self.okta_token_url = f"{[domain](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_domain).rstrip('/')}/oauth2/default/v1/token"
            self.client_id = client_id
            self.client_secret = client_secret
            self.access_token = None
            self.expiry_time = 0
    
        def get_subject_token(self, context, request=None) -> str:
            """Fetches a new token if the current one is expired or missing."""
            if self.access_token and time.time() < self.expiry_time - 60:
                return self.access_token
            self._fetch_okta_access_token()
            return self.access_token
    
        def _fetch_okta_access_token(self):
            """Performs the Client Credentials grant flow with Okta."""
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
            }
            data = {
                "grant_type": "client_credentials",
                "scope": "gcp.test.read",  # Set scope as per Okta app config.
            }
    
            response = requests.post(
                self.okta_token_url,
                headers=headers,
                data=urllib.parse.urlencode(data),
                auth=(self.client_id, self.client_secret),
            )
            response.raise_for_status()
    
            token_data = response.json()
            self.access_token = token_data["access_token"]
            self.expiry_time = time.time() + token_data["expires_in"]
    
    
    def authenticate_with_okta_credentials(
        bucket_name, audience, domain, client_id, client_secret, impersonation_url=None
    ):
        """Authenticates using the custom Okta supplier and gets bucket metadata.
    
        Returns:
            dict: The bucket metadata response from the Google Cloud Storage API.
        """
    
        okta_supplier = OktaClientCredentialsSupplier(domain, client_id, client_secret)
    
        credentials = identity_pool.Credentials(
            audience=audience,
            subject_token_type="urn:ietf:params:oauth:token-type:jwt",
            token_url="https://sts.googleapis.com/v1/token",
            subject_token_supplier=okta_supplier,
            default_scopes=["https://www.googleapis.com/auth/devstorage.read_only"],
            service_account_impersonation_url=impersonation_url,
        )
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(credentials=credentials)
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        return bucket._properties
    
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.json.[GenericJson](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.GenericJson.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.auth.oauth2.[ExternalAccountSupplierContext](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ExternalAccountSupplierContext.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.auth.oauth2.[IdentityPoolCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdentityPoolCredentials.html);
    import com.google.auth.oauth2.[IdentityPoolSubjectTokenSupplier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdentityPoolSubjectTokenSupplier.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.gson.Gson;
    import com.google.gson.JsonSyntaxException;
    import com.google.gson.reflect.TypeToken;
    import java.io.BufferedReader;
    import java.io.DataOutputStream;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.io.Reader;
    import java.lang.reflect.Type;
    import java.net.HttpURLConnection;
    import java.net.URL;
    import java.nio.charset.StandardCharsets;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.time.Instant;
    import java.util.Base64;
    import java.util.Map;
    
      public static [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) authenticateWithOktaCredentials(
          String gcpWorkloadAudience,
          String saImpersonationUrl,
          String gcsBucketName,
          String oktaDomain,
          String oktaClientId,
          String oktaClientSecret)
          throws IOException {
    
        OktaClientCredentialsSupplier oktaSupplier =
            new OktaClientCredentialsSupplier(oktaDomain, oktaClientId, oktaClientSecret);
    
        [IdentityPoolCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdentityPoolCredentials.html).Builder credentialsBuilder =
            [IdentityPoolCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdentityPoolCredentials.html).newBuilder()
                .setAudience(gcpWorkloadAudience)
                // This token type indicates that the subject token is a JSON Web Token (JWT).
                // This is required for Workload Identity Federation with an OIDC provider like Okta.
                .setSubjectTokenType("urn:ietf:params:oauth:token-type:jwt")
                .setTokenUrl("https://sts.googleapis.com/v1/token")
                .[setSubjectTokenSupplier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdentityPoolCredentials.Builder.html#com_google_auth_oauth2_IdentityPoolCredentials_Builder_setSubjectTokenSupplier_com_google_auth_oauth2_IdentityPoolSubjectTokenSupplier_)(oktaSupplier);
    
        if (saImpersonationUrl != null) {
          credentialsBuilder.setServiceAccountImpersonationUrl(saImpersonationUrl);
        }
    
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = credentialsBuilder.build();
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setCredentials(credentials).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        return storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(gcsBucketName);
      }
    
      /**
       * A custom SubjectTokenSupplier that authenticates with Okta using the Client Credentials grant
       * flow.
       */
      private static class OktaClientCredentialsSupplier implements [IdentityPoolSubjectTokenSupplier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdentityPoolSubjectTokenSupplier.html) {
    
        private static final long TOKEN_REFRESH_BUFFER_SECONDS = 60;
    
        private final String oktaTokenUrl;
        private final String clientId;
        private final String clientSecret;
        private String accessToken;
        private Instant expiryTime;
    
        public OktaClientCredentialsSupplier(String domain, String clientId, String clientSecret) {
          // Ensure domain doesn't have a trailing slash for cleaner URL construction
          String cleanedDomain =
              domain.[endsWith](https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStoragePath.html#com_google_cloud_storage_contrib_nio_CloudStoragePath_endsWith_java_lang_String_)("/") ? domain.substring(0, domain.length() - 1) : domain;
          this.oktaTokenUrl = cleanedDomain + "/oauth2/default/v1/token";
          this.clientId = clientId;
          this.clientSecret = clientSecret;
        }
    
        /**
         * Main method called by the auth library. It will fetch a new token if one is not already
         * cached.
         */
        @Override
        public String getSubjectToken([ExternalAccountSupplierContext](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ExternalAccountSupplierContext.html) context) throws IOException {
          // Check if the current token is still valid (with a 60-second buffer).
          boolean isTokenValid =
              this.accessToken != null
                  && this.expiryTime != null
                  && Instant.now().isBefore(this.expiryTime.minusSeconds(TOKEN_REFRESH_BUFFER_SECONDS));
    
          if (isTokenValid) {
            return this.accessToken;
          }
    
          fetchOktaAccessToken();
          return this.accessToken;
        }
    
        /**
         * Performs the Client Credentials grant flow by making a POST request to Okta's token endpoint.
         */
        private void fetchOktaAccessToken() throws IOException {
          URL url = new URL(this.oktaTokenUrl);
          HttpURLConnection conn = (HttpURLConnection) url.openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setRequestProperty("Accept", "application/json");
    
          // The client_id and client_secret are sent in a Basic Auth header.
          String auth = this.clientId + ":" + this.clientSecret;
          String encodedAuth =
              Base64.getEncoder().encodeToString(auth.getBytes(StandardCharsets.UTF_8));
          conn.setRequestProperty("Authorization", "Basic " + encodedAuth);
    
          conn.setDoOutput(true);
          try (java.io.OutputStream out = conn.getOutputStream()) {
            // Scopes define the permissions the access token will have.
            // Update "gcp.test.read" to match your Okta configuration.
            String params = "grant_type=client_credentials&scope=gcp.test.read";
            out.write(params.getBytes(StandardCharsets.UTF_8));
            out.flush();
          }
    
          int responseCode = conn.getResponseCode();
          if (responseCode == HttpURLConnection.HTTP_OK) {
            try (BufferedReader in =
                new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
    
              [GenericJson](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.GenericJson.html) jsonObject =
                  [GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html).getDefaultInstance().createJsonParser(in).parse([GenericJson](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.GenericJson.html).class);
    
              if (jsonObject.containsKey("access_token") && jsonObject.containsKey("expires_in")) {
                this.accessToken = (String) jsonObject.get("access_token");
                Number expiresInNumber = (Number) jsonObject.get("expires_in");
                this.expiryTime = Instant.now().plusSeconds(expiresInNumber.longValue());
              } else {
                throw new IOException("Access token or expires_in not found in Okta response.");
              }
            }
          } else {
            throw new IOException("Failed to authenticate with Okta. Response code: " + responseCode);
          }
        }
      }

## What's next

  * Learn more about [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
