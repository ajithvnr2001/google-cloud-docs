---
url: https://docs.cloud.google.com/spanner-omni/go-cassandra/
title: Use the Cassandra Go client to connect to Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:42.902603+00:00
---

# Use the Cassandra Go client to connect to Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/go-cassandra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use the Cassandra Go client to connect to Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

The Cassandra Go client for Spanner connects applications written for the Apache Cassandra database with Spanner. The client works with Spanner Omni in the same way it works with Spanner. Because Spanner natively supports the Cassandra v4 wire protocol, this client lets Go applications that use the `gocql` driver, or non-Go applications and tools such as `cqlsh`, connect to a Spanner database.

This client acts as a local TCP proxy. It intercepts the raw Cassandra protocol bytes that a driver or client tool sends. It then wraps these bytes and necessary metadata into gRPC messages to communicate with Spanner Omni. The client translates responses from Spanner Omni back into the Cassandra wire format and sends them back to the originating driver or tool.

This document shows how to integrate the client with Spanner Omni using one of the following methods:

  * **In-process dependency** : Use this method for Go applications already using the `gocql` driver. This approach embeds the client within your application process for minimal code modifications.

  * **Sidecar proxy** : Use this method for non-Go applications or when using external Cassandra tools, such as `cqlsh`. This approach runs the client as a standalone process.




For more information about how Apache Cassandra works with Spanner, see [Cassandra interface](https://docs.cloud.google.com/spanner/docs/non-relational/cassandra-overview).

## When to use the Spanner Cassandra Go Client

This client is useful in the following scenarios:

  * **Use Spanner with minimal refactoring.** You want to use Spanner as the backend for your Go application but prefer to keep using the familiar `gocql` API for data access.

  * **Use non-Go Cassandra tools.** You want to connect to Spanner using standard Cassandra tools like `cqlsh` or applications written in other languages that use Cassandra drivers.




## Use the client as an in-process dependency

Go applications connect to Spanner Omni by integrating the Spanner Cassandra Go client as an in-process dependency. This approach embeds the proxy logic directly within your application, which simplifies your deployment architecture by removing the need for a separate process. This configuration also provides optimal performance by avoiding an extra network hop and extra serialization and deserialization of the data.

To use the client as an in-process dependency, do the following:

  * Import the Spanner package in your Go application:
        
        import spanner "github.com/googleapis/go-spanner-cassandra/cassandra/gocql"
        

  * Modify your cluster creation code. Instead of using `gocql.NewCluster`, use `spanner.NewCluster` and provide the following Spanner Omni specific options:

###  Plain text 

The following example shows how to establish a plain-text connection to Spanner Omni:
        
        func main() {
          opts := &spanner.Options{
              // Required: Specify the Spanner database URI
              DatabaseUri: "DATABASE_ID",
          }
          // Optional: Configure Spanner Omni cluster settings as needed
          opts.SpannerEndpoint = "ENDPOINT"
          opts.InstanceType = spanner.Omni
          opts.UsePlainText = true
        
          cluster := spanner.NewCluster(opts)
          // ...
        }
        

###  TLS 

The following example shows how to establish a TLS connection to Spanner Omni:
        
        func main() {
          opts := &spanner.Options{
              // Required: Specify the Spanner database URI
              DatabaseUri: "DATABASE_ID",
          }
          // Optional: Configure Spanner Omni cluster settings as needed
          opts.SpannerEndpoint = "ENDPOINT"
          opts.InstanceType = spanner.Omni
          opts.CaCertificate = "PATH_TO_CA_CRT"
        
          cluster := spanner.NewCluster(opts)
          // ...
        }
        

###  mTLS 

The following example shows how to establish an mTLS connection to Spanner Omni:
        
        func main() {
          opts := &spanner.Options{
              // Required: Specify the Spanner database URI
              DatabaseUri: "DATABASE_ID",
          }
          // Optional: Configure Spanner Omni cluster settings as needed
          opts.SpannerEndpoint = "ENDPOINT"
          opts.InstanceType = spanner.Omni
          opts.CaCertificate = "PATH_TO_CA_CRT"
          opts.ClientCertificate = "PATH_TO_CLIENT_CERT"
          opts.ClientKey = "PATH_TO_CLIENT_KEY"
        
          cluster := spanner.NewCluster(opts)
          // ...
        }
        

Replace the following:

    * `DATABASE_ID`: the ID of your Spanner Omni database, for example, `test-db`.

    * `ENDPOINT`: the endpoint of your Spanner Omni instance, for example, `localhost:15000`.

    * `PATH_TO_CA_CRT`: the path to your CA certificate file.

    * `PATH_TO_CLIENT_CERT`: the path to your client certificate file.

    * `PATH_TO_CLIENT_KEY`: the path to your client key file.




## Deploy the client as a sidecar proxy

Deploying the Spanner Cassandra Go client as a sidecar proxy is an effective option for non-Go applications and tools, such as `cqlsh`, to connect to Spanner Omni using standard Cassandra drivers. This method runs the client as a standalone TCP proxy that intercepts Cassandra wire protocol traffic and translates it into gRPC for communication with Spanner Omni.

This configuration is useful when you need to use external Cassandra tools or when you need to avoid making direct modifications to your application's code.

You can run the sidecar proxy in the following ways:

  * Run locally with the Go `run` command

  * Run with a prebuilt Docker image




### Run locally with the Go `run` command

Running the sidecar proxy as a local process from source code is useful for development and testing environments where you want to quickly iterate on your application and proxy configuration.

  1. Clone the repository:

`git clone https://github.com/googleapis/go-spanner-cassandra.git`

  2. Change to the repository directory:

`cd go-spanner-cassandra`

  3. Run `cassandra_launcher.go` with the required `-db` flag and the following Spanner Omni specific flags:

###  Plain text 

To run with plain-text communication, run the following command:
         
         go run cassandra_launcher.go -db DATABASE_ID -endpoint ENDPOINT -instanceType OMNI -usePlainText
         

###  TLS 

To run with a TLS connection, run the following command:
         
         go run cassandra_launcher.go -db DATABASE_ID -endpoint ENDPOINT -instanceType OMNI -caCertificate PATH_TO_CA_CRT
         

###  mTLS 

To run with an mTLS connection, run the following command:
         
         go run cassandra_launcher.go -db DATABASE_ID -endpoint ENDPOINT -instanceType OMNI -caCertificate PATH_TO_CA_CRT -clientCertificate PATH_TO_CLIENT_CERT -clientKey PATH_TO_CLIENT_KEY
         




### Run with a prebuilt Docker image

We recommend running the sidecar proxy as a containerized application using a prebuilt Docker image for production environments because it provides a consistent and isolated runtime environment.

  1. Pull the image from the official registry repository:

`docker pull gcr.io/cloud-spanner-adapter/cassandra-adapter`

  2. Run the image with the required flags:

###  Plain text 

To run with plain-text communication, run the following command:
         
         docker run -d -p 9042:9042 gcr.io/cloud-spanner-adapter/cassandra-adapter -db DATABASE_ID -endpoint ENDPOINT -instanceType OMNI -usePlainText
         

###  TLS 

To run with a TLS connection, run the following command:
         
         docker run -d -p 9042:9042 gcr.io/cloud-spanner-adapter/cassandra-adapter -db DATABASE_ID -endpoint ENDPOINT -instanceType OMNI -caCertificate PATH_TO_CA_CRT
         

###  mTLS 

To run with an mTLS connection, run the following command:
         
         docker run -d -p 9042:9042 gcr.io/cloud-spanner-adapter/cassandra-adapter -db DATABASE_ID -endpoint ENDPOINT -instanceType OMNI -caCertificate PATH_TO_CA_CRT -clientCertificate PATH_TO_CLIENT_CERT -clientKey PATH_TO_CLIENT_KEY
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
