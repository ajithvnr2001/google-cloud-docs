---
url: https://docs.cloud.google.com/bigtable/docs/samples-python-hello-happybase/
title: HappyBase API hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:04.917931+00:00
---

# HappyBase API hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-python-hello-happybase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HappyBase API hello world

**Alpha**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This example is a very simple "hello world" application, written in Python, that illustrates how to:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.



## Set up authentication

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

## Running the sample

This example uses the [HappyBase package](https://google-cloud-python-happybase.readthedocs.io/en/latest/) of the [Google Cloud Client Library for Python](https://docs.cloud.google.com/python/docs/reference), an implementation of the [HappyBase](http://happybase.readthedocs.io/en/stable/) APIs, to communicate with Bigtable. Use the HappyBase package if you need to move an existing HBase workload to Bigtable. For new applications, see the ["hello world" example that uses the Bigtable package](https://docs.cloud.google.com/bigtable/docs/samples-python-hello).

To run this sample program, follow the [instructions for the sample on GitHub](https://github.com/googleapis/python-bigtable/tree/master/samples/hello_happybase).

## Using the HappyBase APIs with Bigtable

The sample application connects to Bigtable and demonstrates some simple operations.

### Installing and importing the client library

The required Python packages can be installed using [PIP](https://pip.pypa.io/en/stable/) into a [virtualenv environment](https://virtualenv.pypa.io/en/stable/). The sample includes a [requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files) defining the needed packages.
    
    
    google-cloud-happybase==0.33.0
    six==1.17.0 # See https://github.com/googleapis/google-cloud-python-happybase/issues/128
    

The modules can then be imported.
    
    
    from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    from google.cloud import happybase
    

### Connecting to Bigtable

Connect to Bigtable by passing a [`bigtable.Client`](https://docs.cloud.google.com/python/docs/reference/bigtable/latest) to a [`happybase.Connection`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-connection.html).
    
    
    # The client must be created with admin=True because it will create a
    # table.
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    connection = happybase.Connection(instance=instance)

### Creating a table

Use [`Connection.create_table()`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-connection.html#google.cloud.happybase.connection.Connection.create_table) to create a table and its column families.

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
    print("Creating the {} table.".format(table_name))
    column_family_name = "cf1"
    connection.create_table(
        table_name, {column_family_name: dict()}  # Use default options.
    )

### Writing rows to a table

Get an existing [`Table`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-table.html) with [`Connection.table()`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-connection.html#google.cloud.happybase.connection.Connection.table). Use [`Table.put()`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-table.html#google.cloud.happybase.table.Table.put) to write a row to the table.
    
    
    print("Writing some greetings to the table.")
    table = connection.table(table_name)
    column_name = "{fam}:greeting".format(fam=column_family_name)
    greetings = [
        "Hello World!",
        "Hello Cloud Bigtable!",
        "Hello HappyBase!",
    ]
    
    for i, value in enumerate(greetings):
        # Note: This example uses sequential numeric IDs for simplicity,
        # but this can result in poor performance in a production
        # application.  Since rows are stored in sorted order by key,
        # sequential keys can result in poor distribution of operations
        # across nodes.
        #
        # For more information about how to design a Bigtable schema for
        # the best performance, see the documentation:
        #
        #     https://cloud.google.com/bigtable/docs/schema-design
        row_key = "greeting{}".format(i)
        table.put(row_key, {column_name.encode("utf-8"): value.encode("utf-8")})

### Reading a row by its key

Get a row directly using its key with [`Table.row()`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-table.html#google.cloud.happybase.table.Table.row).
    
    
    print("Getting a single greeting by row key.")
    key = "greeting0".encode("utf-8")
    row = table.row(key)
    print("\t{}: {}".format(key, row[column_name.encode("utf-8")]))

### Scanning all table rows

Use [`Table.scan()`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-table.html#google.cloud.happybase.table.Table.scan) to get a range of rows.
    
    
    print("Scanning for all greetings:")
    
    for key, row in table.scan():
        print("\t{}: {}".format(key, row[column_name.encode("utf-8")]))

### Deleting a table

Delete a table with [`Connection.delete_table()`](https://google-cloud-python-happybase.readthedocs.io/en/latest/happybase-connection.html#google.cloud.happybase.connection.Connection.delete_table).
    
    
    print("Deleting the {} table.".format(table_name))
    connection.delete_table(table_name)

## Putting it all together

Here is the full example without comments.
    
    
    
    """Demonstrates how to connect to Cloud Bigtable and run some basic operations.
    
    Prerequisites:
    
    - Create a Cloud Bigtable cluster.
      https://cloud.google.com/bigtable/docs/creating-cluster
    - Set your Google Application Default Credentials.
      https://developers.google.com/identity/protocols/application-default-credentials
    """
    
    import argparse
    from ..utils import wait_for_table
    
    from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    from google.cloud import happybase
    
    
    
    def main(project_id, instance_id, table_name):
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        connection = happybase.Connection(instance=instance)
    
        try:
            print("Creating the {} table.".format(table_name))
            column_family_name = "cf1"
            connection.create_table(
                table_name, {column_family_name: dict()}  # Use default options.
            )
    
            wait_for_table(instance.table(table_name))
    
            print("Writing some greetings to the table.")
            table = connection.table(table_name)
            column_name = "{fam}:greeting".format(fam=column_family_name)
            greetings = [
                "Hello World!",
                "Hello Cloud Bigtable!",
                "Hello HappyBase!",
            ]
    
            for i, value in enumerate(greetings):
                row_key = "greeting{}".format(i)
                table.put(row_key, {column_name.encode("utf-8"): value.encode("utf-8")})
    
            print("Getting a single greeting by row key.")
            key = "greeting0".encode("utf-8")
            row = table.row(key)
            print("\t{}: {}".format(key, row[column_name.encode("utf-8")]))
    
            print("Scanning for all greetings:")
    
            for key, row in table.scan():
                print("\t{}: {}".format(key, row[column_name.encode("utf-8")]))
    
        finally:
            print("Deleting the {} table.".format(table_name))
            connection.delete_table(table_name)
            connection.close()
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        parser.add_argument("project_id", help="Your Cloud Platform project ID.")
        parser.add_argument(
            "instance_id", help="ID of the Cloud Bigtable instance to connect to."
        )
        parser.add_argument(
            "--table", help="Table to create and destroy.", default="Hello-Bigtable"
        )
    
        args = parser.parse_args()
        main(args.project_id, args.instance_id, args.table)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
