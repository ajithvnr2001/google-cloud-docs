---
url: https://docs.cloud.google.com/storage/docs/aws-simple-migration/
title: Simple migration from Amazon S3 to Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:56.971962+00:00
---

# Simple migration from Amazon S3 to Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/aws-simple-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Simple migration from Amazon S3 to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to complete a simple migration from Amazon Simple Storage Service (Amazon S3) to Cloud Storage. In a simple migration, you use your existing tools and libraries for generating authenticated REST requests to Amazon S3 to send authenticated requests to Cloud Storage instead.

If you are new to Cloud Storage and won't be using the API directly, consider [using the Google Cloud console to set up and manage transfers](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-console). The Google Cloud console provides a graphical interface to Cloud Storage that lets you accomplish many of your storage tasks using just a browser, including migration of your data from Amazon S3 to Cloud Storage.

If you want Cloud Storage to store a backup of your Amazon S3 data, consider using [event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers), which use Amazon S3 Event Notifications to automatically keep a Cloud Storage bucket in sync with your Amazon S3 source.

## Migrate from Amazon S3 to Cloud Storage in a simple migration scenario

In order to make requests to Cloud Storage, you need to complete the following steps:

  * Set a default Google Cloud project.
  * Get an [HMAC (hash-based message authentication code) key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).
  * In your existing tools or libraries, make the following changes:

    * Change the request endpoint to use the Cloud Storage [XML API request endpoint](https://docs.cloud.google.com/storage/docs/request-endpoints#xml-api).
    * Replace the Amazon Web Services (AWS) access and secret key with the corresponding Cloud Storage access ID and secret (collectively called your Cloud Storage HMAC key).
    * Make sure your `x-amz-` headers use supported Cloud Storage values. For example, `x-amz-storage-class` should use one of the available [Cloud Storage storage classes](https://docs.cloud.google.com/storage/docs/storage-classes).

When you use the Cloud Storage XML API in a simple migration scenario, specifying the `AWS` signature identifier in the `Authorization` header lets Cloud Storage know to expect `x-amz-*` headers and Amazon S3 ACL XML syntax in your request. Cloud Storage processes `x-amz-*` headers that have an `x-goog-*` equivalent, such as those listed in the [headers table](https://docs.cloud.google.com/storage/docs/migrating#custommeta), and it processes the [`x-amz-decoded-content-length` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xamzdecodedcontentlength).




After you make these changes, you can start using your existing tools and libraries to send HMAC requests to Cloud Storage.

For example, the following samples demonstrate how to list Cloud Storage buckets using the Amazon S3 SDK:

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"github.com/aws/aws-sdk-go/aws"
    	"github.com/aws/aws-sdk-go/aws/credentials"
    	"github.com/aws/aws-sdk-go/aws/session"
    	"github.com/aws/aws-sdk-go/service/s3"
    )
    
    func listGCSBuckets(w io.Writer, googleAccessKeyID string, googleAccessKeySecret string) error {
    	// googleAccessKeyID := "Your Google Access Key ID"
    	// googleAccessKeySecret := "Your Google Access Key Secret"
    
    	// Create a new client and do the following:
    	// 1. Change the endpoint URL to use the Google Cloud Storage XML API endpoint.
    	// 2. Use Cloud Storage HMAC Credentials.
    	sess := session.Must(session.NewSession(&aws.Config{
    		Region:      aws.String("auto"),
    		Endpoint:    aws.String("https://storage.googleapis.com"),
    		Credentials: credentials.NewStaticCredentials(googleAccessKeyID, googleAccessKeySecret, ""),
    	}))
    
    	client := s3.New(sess)
    	ctx := context.Background()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    	result, err := client.ListBucketsWithContext(ctx, &s3.ListBucketsInput{})
    	if err != nil {
    		return fmt.Errorf("ListBucketsWithContext: %w", err)
    	}
    
    	fmt.Fprintf(w, "Buckets:")
    	for _, b := range result.Buckets {
    		fmt.Fprintf(w, "%s\n", aws.StringValue(b.Name))
    	}
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.amazonaws.auth.AWSStaticCredentialsProvider;
    import com.amazonaws.auth.BasicAWSCredentials;
    import com.amazonaws.client.builder.AwsClientBuilder;
    import com.amazonaws.services.s3.AmazonS3;
    import com.amazonaws.services.s3.AmazonS3ClientBuilder;
    import com.amazonaws.services.s3.model.Bucket;
    import java.util.List;
    
    public class ListGcsBuckets {
      public static void listGcsBuckets(String googleAccessKeyId, String googleAccessKeySecret) {
    
        // String googleAccessKeyId = "your-google-access-key-id";
        // String googleAccessKeySecret = "your-google-access-key-secret";
    
        // Create a BasicAWSCredentials using Cloud Storage HMAC credentials.
        BasicAWSCredentials googleCreds =
            new BasicAWSCredentials(googleAccessKeyId, googleAccessKeySecret);
    
        // Create a new client and do the following:
        // 1. Change the endpoint URL to use the Google Cloud Storage XML API endpoint.
        // 2. Use Cloud Storage HMAC Credentials.
        AmazonS3 interopClient =
            AmazonS3ClientBuilder.standard()
                .withEndpointConfiguration(
                    new AwsClientBuilder.EndpointConfiguration(
                        "https://storage.googleapis.com", "auto"))
                .withCredentials(new AWSStaticCredentialsProvider(googleCreds))
                .build();
    
        // Call GCS to list current buckets
        List<Bucket> buckets = interopClient.listBuckets();
    
        // Print bucket names
        System.out.println("Buckets:");
        for (Bucket bucket : buckets) {
          System.out.println(bucket.getName());
        }
    
        // Explicitly clean up client resources.
        interopClient.shutdown();
      }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import boto3  # type: ignore
    
    
    def list_gcs_buckets(
        google_access_key_id: str, google_access_key_secret: str
    ) -> List[str]:
        """Lists all Cloud Storage buckets using AWS SDK for Python (boto3)
        Positional arguments:
            google_access_key_id: hash-based message authentication code (HMAC) access ID
            google_access_key_secret: HMAC access secret
    
        Returned value is a list of strings, one for each bucket name.
    
        To use this sample:
        1. Create a Cloud Storage HMAC key: https://cloud.google.com/storage/docs/authentication/managing-hmackeys#create
        2. Change endpoint_url to a Google Cloud Storage XML API endpoint.
    
        To learn more about HMAC: https://cloud.google.com/storage/docs/authentication/hmackeys#overview
        """
        client = boto3.client(
            "s3",
            region_name="auto",
            endpoint_url="https://storage.googleapis.com",
            aws_access_key_id=google_access_key_id,
            aws_secret_access_key=google_access_key_secret,
        )
    
        # Call GCS to list current buckets
        response = client.list_buckets()
    
        # Return list of bucket names
        results = []
        for bucket in response["Buckets"]:
            results.append(bucket["Name"])
            print(bucket["Name"])  # Can remove if not needed after development
        return results
    
    

## Set a default project

To use Cloud Storage in a simple migration scenario, it's recommended that you set a default [project](https://docs.cloud.google.com/storage/docs/projects), which Cloud Storage uses to perform [certain operations](https://docs.cloud.google.com/storage/docs/projects#projectid-using), such as `GET` service or `PUT` bucket. If you don't set a default project, you must specify a project header. in certain requests.

**Important:** Because the simple migration scenario uses HMAC keys, make sure that the project you migrate to isn't subject to the [`restrictAuthTypes` constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-auth-types) for the account type you intend to use.

To set a default project:

  1. [Open the **Cloud Storage Settings** page](https://console.cloud.google.com/storage/settings) in the Google Cloud console.
  2. Select the **Interoperability** tab.
  3. Click **Set PROJECT-ID as default project**, located in the section _Default project for interoperable access_.

If the project is already the default project, you see **PROJECT-ID is your default project for interoperable access**.




This project is now your default project. You can change your default project at any time by choosing a different project and following these steps.

### Alternatively specify a project header

Instead of, or in addition to, setting a default project, you can use the `x-amz-project-id` header in individual requests that require you to specify a project.

  * A request that uses `x-amz-project-id` uses the project specified in the header, even if there is an existing default project.



The `x-amz-project-id` header is useful when:

  * You're working with multiple projects.
  * Your requests are made by a service account associated with a different project, because service accounts use their parent project as the default project.



Note that Amazon S3 does not have [projects](https://docs.cloud.google.com/storage/docs/projects), so depending on the tools or client libraries you use, specifying a `x-amz-project-id` header may not be an option. In this case, you should set a default project.

## Use HMAC keys

To use the Cloud Storage XML API in a simple migration scenario, use Cloud Storage [hash-based message authentication code (HMAC) keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) for the credentials. Typically, you should [create an HMAC key](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys) that is associated with a service account; however, you can alternatively use one associated with a user account.

## Authenticate in a simple migration scenario

### Use the Authorization header

For operations in a simple migration scenario that require authentication, you include an `Authorization` request header just like you do for requests to Amazon S3. The `Authorization` header syntax for an Amazon S3 request is:
    
    
    Authorization: AWS4-HMAC-SHA256 Credential=AWS-ACCESS-KEY/CREDENTIAL_SCOPE, SignedHeaders=SIGNED_HEADERS, Signature=SIGNATURE
    

In a simple migration scenario, you only change the header to use your Cloud Storage HMAC access ID and make sure the `Signature` you attach is calculated with your Cloud Storage HMAC secret key:
    
    
    Authorization: ALGORITHM Credential=GOOG-ACCESS-ID/CREDENTIAL_SCOPE, SignedHeaders=SIGNED_HEADERS, Signature=SIGNATURE
    

The parts of the `Authorization` header are:

  * ALGORITHM: The signature algorithm and version that you are using. Using `AWS4-HMAC-SHA256` indicates that you are using an HMAC V4 signature and you intend to send `x-amz-*` headers. You can also use `GOOG4-HMAC-SHA256`, which indicates that you are using an HMAC V4 signature and you intend to send `x-goog-*` headers, or `GOOG4-RSA-SHA256`, which indicates that you are using an RSA V4 signature and you intend to send `x-goog-*` headers.

  * GOOG-ACCESS-ID: The access ID identifies the entity that is making and signing the request. In a simple migration, replace the Amazon Web Service (AWS) access key ID you use to access Amazon S3 with your Cloud Storage HMAC access ID. Your Cloud Storage HMAC access ID starts with `GOOG`.

  * CREDENTIAL_SCOPE: The credential scope, as [defined in the signature](https://docs.cloud.google.com/storage/docs/authentication/signatures#credential-scope). In a simple migration, you don't need to change credential scope if you are using `AWS4-HMAC-SHA256` for your ALGORITHM value.

  * SIGNED_HEADERS: A semicolon-separated list of names of headers that must be included to sign this request. All headers should be lowercase and sorted by character code.

An example of an Amazon S3-style signed header string looks like:
        
        content-type;host;x-amz-date

In a simple migration, you don't need to make any changes to the signed header string.

  * SIGNATURE: The [signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) that allows the request to be authenticated. In a simple migration, replace the AWS access key information with the equivalent Cloud Storage HMAC key information.




### Sample authentication request

The following examples upload an object named `/europe/france/paris.jpg` to a bucket named `my-travel-maps`, apply the predefined ACL `public-read`, and define a custom metadata header for reviewers. Here is the request to a bucket in Amazon S3:
    
    
    PUT europe/france/paris.jpg HTTP/1.1
    Host: my-travel-maps.s3.amazonaws.com
    Date: Mon, 11 Mar 2019 23:46:19 GMT
    Content-Length: 888814
    Content-Type: image/jpg
    x-amz-acl: public-read
    x-amz-date:20190311T192918Z
    x-amz-meta-reviewer: joe,jane
    Authorization: AWS4-HMAC-SHA256 Credential=AWS-ACCESS-KEY/20190311/us-east-1/s3/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-acl;x-amz-date;x-amz-meta-reviewer, Signature=SIGNATURE
    

Here is the request for a bucket in Cloud Storage:
    
    
    PUT europe/france/paris.jpg HTTP/1.1
    Host: my-travel-maps.storage.googleapis.com
    Date: Mon, 11 Mar 2019 23:46:19 GMT
    Content-Length: 888814
    Content-Type: image/jpg
    x-amz-acl: public-read
    x-amz-date:20190311T192918Z
    x-amz-meta-reviewer: joe,jane
    Authorization: AWS4-HMAC-SHA256 Credential=GOOG-ACCESS-ID/20190311/us-east-1/s3/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-acl;x-amz-date;x-amz-meta-reviewer, Signature=SIGNATURE
    

Here is the corresponding canonical request that was created for this request:
    
    
    PUT
    /europe/france/paris.jpg
    
    content-length:888814
    content-type:image/jpg
    host:my-travel-maps.storage.googleapis.com
    x-amz-acl:public-read
    x-amz-date:20190311T192918Z
    x-amz-meta-reviewer:joe,jane
    
    content-length,content-type,host,x-amz-acl,x-amz-date,x-amz-meta-reviewer
    82e3da8b3f35989512e8d428add7eca73ab0e5f36586e66fbad8e1051343cbd2
    

Here is the corresponding string-to-sign that was created for this request:
    
    
    AWS4-HMAC-SHA256
    20190311T192918Z
    20190311/us-east-1/s3/aws4_request
    73918a5ff373d7a03e406fbf9ea35675396b06fca2af76c27a5c451fa783ef65
    

This request did not provide a Content-MD5 header, so an empty string is shown in the second line of the message.

## Access control in a simple migration scenario

To support simple migrations, Cloud Storage accepts ACLs produced by Amazon S3. In a simple migration scenario, you use `AWS` as your signature identifier, which tells Cloud Storage to expect ACL syntax using Amazon S3 ACL XML syntax. You should ensure that the Amazon S3 ACLs you use map to the Cloud Storage ACL model. For example, if your tools and libraries use Amazon S3's ACL syntax to grant bucket `WRITE` permission, then they must also grant bucket `READ` permission because Cloud Storage permissions are [concentric](https://docs.cloud.google.com/storage/docs/access-control/lists#concentric). You do not need to specify both `WRITE` and `READ` permission when you grant `WRITE` permission using the Cloud Storage syntax.

Cloud Storage supports Amazon S3 ACL syntax in the following scenarios:

  * In a request to Cloud Storage to retrieve ACLs (for example, a `GET` Object or `GET` Bucket request), Cloud Storage returns Amazon S3 ACL syntax.
  * In a request to Cloud Storage to apply ACLs (for example, a `PUT` Object or `PUT` Bucket request), Cloud Storage expects to receive Amazon S3 ACL syntax.



The `Authorization` header in a simple migration scenario uses `AWS` for the signature identifier, but with your Cloud Storage HMAC access ID.
    
    
    Authorization: AWS4-HMAC-SHA256 Credential=GOOG-ACCESS-ID/CREDENTIAL_SCOPE, SignedHeaders=SIGNED_HEADERS, Signature=SIGNATURE
    

The following example shows a `GET` request to Cloud Storage to return the ACLs for an object.
    
    
    GET europe/france/paris.jpg?acl HTTP/1.1
    Host: my-travel-maps.storage.googleapis.com
    Date: Thu, 21 Feb 2019 23:50:10 GMT
    Content-Type: application/xml
    X-Amz-Date: 20190221T235010Z
    Authorization: AWS4-HMAC-SHA256 Credential=GOOGMC5PDPA5JLZYQMHQHRAX/20190221/region/s3/aws4_request, SignedHeaders=host;x-amz-date, Signature=29088b1d6dfeb2549f6ff67bc3744abb7e45475f0ad60400485805415bbfc534
    

The response to the request includes the ACL using Amazon S3 ACL syntax.
    
    
    <?xml version='1.0' encoding='UTF-8'?>
    <AccessControlPolicy>
        <Owner>
            <ID>00b4903a972faa8bcce9382686e9129676f1cd6e5def1f5663affc2ba4652490
            </ID>
            <DisplayName>OwnerName</DisplayName>
        </Owner>
        <AccessControlList>
            <Grant>
                <Grantee xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
                    xsi:type='CanonicalUser'>
                    <ID>00b4903a972faa8bcce9382686e9129676f1cd6e5def1f5663affc2ba4652490</ID>
                    <DisplayName>UserName</DisplayName>
                </Grantee>
                <Permission>FULL_CONTROL</Permission>
            </Grant>
        </AccessControlList>
    </AccessControlPolicy>
    

The following example shows a `PUT` request to Cloud Storage to set the ACLs for an object. The example shows a request body with Amazon S3 ACL syntax.
    
    
    PUT europe/france/paris.jpg?acl HTTP/1.1
    Host: my-travel-maps.storage.googleapis.com
    Date: Thu, 21 Feb 2019 23:50:10 GMT
    Content-Type: application/xml
    Content-Length: 337
    X-Amz-Date: 20190221T235010Z
    Authorization: AWS4-HMAC-SHA256 Credential=GOOGMC5PDPA5JLZYQMHQHRAX/20190221/region/s3/aws4_request, SignedHeaders=host;x-amz-date, Signature=29088b1d6dfeb2549f6ff67bc3744abb7e45475f0ad60400485805415bbfc534
    
    <?xml version='1.0' encoding='utf-8'?>
    <AccessControlPolicy>
      <AccessControlList>
        <Grant>
          <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="AmazonCustomerByEmail">
            <EmailAddress>jeffersonloveshiking@gmail.com</EmailAddress>
          </Grantee>
          <Permission>FULL_CONTROL</Permission>
        </Grant>
      </AccessControlList>
    </AccessControlPolicy>
    

Finally, in a simple migration scenario, you can also use the `GOOG1` signature identifier in the `Authorization` header. In this case, you must use the Cloud Storage ACL syntax and ensure that all of your `x-amz-*` headers are changed to `x-goog-*`. While this is possible, we recommend that you choose a [full migration](https://docs.cloud.google.com/storage/docs/migrating) in order to use all the benefits of Cloud Storage.

## Support for XML API compatibility with Amazon S3

For discussions about XML API interoperability, see Stack Overflow using the tag [google-cloud-storage](http://stackoverflow.com/questions/tagged/google-cloud-storage).

## What's next

  * [Plan a migration from Amazon S3](https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage).
  * [Transfer your data to Cloud Storage from external sources](https://docs.cloud.google.com/storage-transfer/docs/create-transfers), such as Amazon S3 and Microsoft Azure Blob Storage, using Storage Transfer Service.
  * [Create event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers) that use Amazon S3 Event Notifications to keep a Cloud Storage bucket in sync with Amazon S3.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
