---
url: https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py/
title: Send RPC requests with Python \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:36:08.513314+00:00
---

# Send RPC requests with Python  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Send RPC requests with Python Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

Applications can interact with the Universal Ledger API using gRPC and Python. This approach involves generating and using Python client libraries compiled from the service's protocol buffer definitions.

This tutorial shows developers who want to implement a client for the Universal Ledger API how to set up a suitable development environment, generate the necessary libraries, and make a gRPC call using Python.

## Before you begin

To complete this tutorial you will need:

  * A Google Cloud project with the Universal Ledger API enabled.

  * An IAM role such as `universalledger.googleapis.com/endpointViewer` so you can at least view Universal Ledger endpoints.

  * Local authentication credentials for your user account. Run the following command to configure these credentials:
        
        gcloud auth application-default login




To learn more about these steps, see the [Preview onboarding](https://cloud.google.com/universal-ledger/preview-onboarding) guide.

## Set up your environment

The instructions in this tutorial are written for an environment running Ubuntu 25.04, which includes Python 3.13 by default. You might need to modify the commands if you are using a different operating system.

To set up your development environment, complete the following steps. These steps guide you through installing necessary command-line tools. This includes using `pipx` to install `grpcio-tools`, which is used to build the gRPC bindings. To isolate Python dependencies for this project, you will also create and activate a Python virtual environment, and then install the required Python libraries into it using `pip`.

  1. Install the base dependencies using the commands:
         
         sudo apt update
         sudo apt install git pipx python3.13-venv

  2. Use `pipx` to install the gRPC tools application and ensure that its binary directory is added to your `PATH`:
         
         pipx install grpcio-tools
         pipx ensurepath

Close and reopen your terminal to complete the activation of `pipx`.

  3. Create a parent directory to hold the files of this tutorial.
         
         mkdir gcul_tutorial
         cd gcul_tutorial

Unless specified otherwise, the remaining commands should be run from within this new directory.

  4. Create a Python virtual environment and install the remaining libraries:
         
         python3 -m venv example_client
         cd example_client
         source ./bin/activate
         pip3 install google-auth googleapis-common-protos grpcio requests
         cd ..

Those libraries are:

     * `google-auth`: for handling Google Cloud authentication.
     * `googleapis-common-protos`: common protocol buffer messages used across Google APIs.
     * `grpcio`: the gRPC library for Python.
     * `requests`: needed by some of the dependencies to send HTTP requests.



## Generate the Protocol Buffer libraries

To interact with the Universal Ledger API using gRPC, your Python application needs client libraries compiled from the service's [Protocol Buffer](https://developers.google.com/protocol-buffers) (`.proto`) definitions. These definitions specify the API's services, methods, and message types.

This section shows you how to download these `.proto` files from the `googleapis` repository and use the installed `grpcio-tools` to generate the necessary Python source code.

  1. Clone the [googleapis](https://github.com/googleapis/googleapis/) GitHub repository where Protocol Buffer definitions for Google APIs are published.
         
         git clone https://github.com/googleapis/googleapis.git

  2. Build the Protocol Buffer definitions and gRPC bindings for the Universal Ledger API.
         
         python-grpc-tools-protoc --proto_path=googleapis/ \
             --python_out=example_client \
             --pyi_out=example_client \
             --grpc_python_out=example_client \
             google/cloud/universalledger/v1/universalledger.proto
         python-grpc-tools-protoc --proto_path=googleapis/ \
             --python_out=example_client \
             --pyi_out=example_client \
             google/cloud/universalledger/v1/query.proto
         python-grpc-tools-protoc --proto_path=googleapis/ \
             --python_out=example_client \
             --pyi_out=example_client \
             google/cloud/universalledger/v1/accounts.proto
         python-grpc-tools-protoc --proto_path=googleapis/ \
             --python_out=example_client \
             --pyi_out=example_client \
             google/cloud/universalledger/v1/common.proto
         python-grpc-tools-protoc --proto_path=googleapis/ \
             --python_out=example_client \
             --pyi_out=example_client \
             google/cloud/universalledger/v1/transactions.proto
         python-grpc-tools-protoc --proto_path=googleapis/ \
             --python_out=example_client \
             --pyi_out=example_client \
             google/cloud/universalledger/v1/types.proto
         python-grpc-tools-protoc --proto_path=googleapis/ \
             --python_out=example_client \
             --pyi_out=example_client \
             google/cloud/universalledger/v1/status_event.proto

This should create several files under the `example_client/google/cloud/universalledger/v1` directory.
         
         accounts_pb2.py
         accounts_pb2.pyi
         common_pb2.py
         common_pb2.pyi
         query_pb2.py
         query_pb2.pyi
         status_event_pb2.py
         status_event_pb2.pyi
         transactions_pb2.py
         transactions_pb2.pyi
         types_pb2.py
         types_pb2.pyi
         universalledger_pb2.py
         universalledger_pb2.pyi
         universalledger_pb2_grpc.py
         




## Call the Universal Ledger API

Finally, create a Python script to call the Universal Ledger API using the generated libraries. Save the following code as `example_client/endpoints.py`.

In the code, replace the following placeholder values:

  * `PROJECT_ID`: your Google Cloud project ID–for example, `my-project`.
  * `REGION`: the Google Cloud region where your Universal Ledger endpoint is located–for example, `us-east5`.


    
    
    """Example calling the Universal Ledger API."""
    
    import sys
    
    import google.auth
    import google.auth.transport.grpc
    import google.auth.transport.requests
    from google.cloud.universalledger.v1 import universalledger_pb2
    from google.cloud.universalledger.v1 import universalledger_pb2_grpc
    import grpc
    
    PROJECT = "PROJECT_ID"
    REGION = "REGION"
    API_ENDPOINT = f"universalledger.{REGION}.rep.googleapis.com"
    SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
    
    
    def main() -> str | None:
      # Get the application default credentials.
      credentials, _ = google.auth.default(scopes=SCOPES)
    
      # Get an HTTP request function to refresh credentials.
      refresh_request = google.auth.transport.requests.Request()
    
      # Create a secure channel to the API endpoint.
      with google.auth.transport.grpc.secure_authorized_channel(
          credentials, refresh_request, API_ENDPOINT
      ) as channel:
        # Create the client stub using the generated code.
        stub = universalledger_pb2_grpc.UniversalLedgerStub(channel)
    
        # Parent location for GCUL network endpoints.
        parent = f"projects/{PROJECT}/locations/{REGION}"
    
        # Build the request message.
        request = universalledger_pb2.ListEndpointsRequest(parent=parent)
    
        # Make the gRPC call.
        try:
          metadata = [("x-goog-request-params", f"parent={parent}")]
          response = stub.ListEndpoints(request, metadata=metadata)
        except grpc.RpcError as exc:
          return f"{exc.code().name}: {exc.details()}"
    
        if not response.endpoints:
          return f"No endpoints found under: {parent}"
    
        print("Found the following endpoints:")
        for endpoint in response.endpoints:
          print("-", endpoint.name)
    
    
    if __name__ == "__main__":
      sys.exit(main())
    

To run the script, navigate into the `example_client` directory. The virtual environment should still be active from the setup steps.

  1. Change to the script directory:
         
         cd example_client
         

Your shell prompt should confirm the virtual environment is active (for example, it is prefixed with `(example_client)`).

  2. Run the Python script:
         
         python3 endpoints.py
         




You should see an output such as:
    
    
    Found the following endpoints:
    - projects/my-project/locations/us-east5/endpoint/gcul-pilot-testing
    - projects/my-project/locations/us-east5/endpoint/gcul-user-testing
    

## What's next

  * See [all methods in the Universal Ledger API](https://docs.cloud.google.com/universal-ledger/reference/rpc).
  * Learn about [gRPC support in other languages](https://grpc.io/docs/languages/).
  * Explore the [Universal Ledger API protocol buffer definitions](https://github.com/googleapis/googleapis/tree/master/google/cloud/universalledger/v1).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
