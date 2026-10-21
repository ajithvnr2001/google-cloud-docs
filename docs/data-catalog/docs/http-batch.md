---
url: https://docs.cloud.google.com/data-catalog/docs/http-batch/
title: Creating HTTP batch requests for Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:46:13.224205+00:00
---

# Creating HTTP batch requests for Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/http-batch/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  Creating HTTP batch requests for Data Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Each HTTP connection that your application makes requires a certain amount of overhead. Data Catalog API requests support batching, and lets you combine several API calls into a single HTTP request. If you have many small requests to make and want to minimize HTTP request overhead, you might want to use HTTP batching.

**Note:** Batching reduces overhead, but requests within a batch still count as multiple requests for API quota purposes.

For more information about using HTTP batch with Google Cloud, see the [Google API Python client documentation](https://github.com/googleapis/google-api-python-client/blob/master/docs/batch.md).

**Note:** You're limited to 1000 calls in a single batch request. If you need to make more calls than that, use multiple batch requests.

## Creating HTTP batch requests in Python

To use batch requests to create or manipulate entries in Data Catalog, you first need to search for the entries you want to change using [`catalog.search()`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/catalog/search) or [`entries.lookup()`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/entries/lookup).

Next, follow these steps to build an HTTP batch request using the [Google Python API](https://github.com/googleapis/google-api-python-client/blob/master/docs/batch.md):

  1. Create a [`BatchHttpRequest`](https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.http.BatchHttpRequest-class.html) object by calling `new_batch_http_request()` or with the `BatchHttpRequest()` constructor. You might pass in a callback, which will be called in response to each request.
  2. Call `add()` on the `BatchHttpRequest` object for each request you want to execute. If you passed a callback when creating your `BatchHttpRequest` object, each `add()` might include parameters to be passed to the callback.
  3. After you've added the requests, call `execute()` on the `BatchHttpRequest` object to execute them. The `execute()` function blocks until all callbacks have been called.



Requests in a `BatchHttpRequest` might be executed in parallel, and not in the order of execution. This means requests in the same batch shouldn't be dependent on each other. For example, you shouldn't create an `EntryGroup` and `Entry` belonging to it in the same request, as the creation of the `Entry` might execute before the creation of the `EntryGroup`, causing execution to fail.

### Batch requests with locational endpoints

When using HTTP batch requests with Data Catalog [locational API endpoints](https://docs.cloud.google.com/data-catalog/docs/concepts/regions), all API requests in a batch must belong to the same region. When executing the batch, you must call the correct locational endpoint. For example, if your resources are in `us-central1`, call `https://us-central1-datacatalog.googleapis.com/batch`.

**Note:** Here "region" refers to standard regions as well as multi-regions like "Global", "European Union", and "United States".

#### Region-independent APIs

Region-independent APIs, such as `catalog.lookup` and `entries.search`, can be grouped with each other, but must not be grouped with region-dependent APIs. For region-independent APIs, use the endpoint: `https://datacatalog.googleapis.com/batch`.

## Example

This sample Python application demonstrates how to use an HTTP batch request to create multiple tags from a tag template using the Data Catalog API.
    
    
    from googleapiclient.discovery import build
    from googleapiclient.http import BatchHttpRequest
    from oauth2client.service_account import ServiceAccountCredentials
    import uuid
    
    #-------------------------------------------------------------#
    # 0. Helper and initialization logic
    #-------------------------------------------------------------#
    
    # Set the environment configuration.
    service_key_file_location = '[SA_PATH]'
    
    project_id = '[MY_PROJECT_ID]'
    
    # Helper container to store results.
    class DataContainer:
        def __init__(self):
            self.data = {}
    
        def callback(self, request_id, response, exception):
            if exception is not None:
                print('request_id: {}, exception: {}'.format(request_id, str(exception)))
                pass
            else:
                print(request_id)
                self.data[request_id] = response
    
    # Helper function to build the Discovery Service config.
    def get_service(api_name, api_version, scopes, key_file_location):
        """
        Get a service that communicates to a Google API.
    
        Args:
            api_name: The name of the API to connect to.
            api_version: The API version to connect to.
            scopes: A list auth scopes to authorize for the application.
            key_file_location: The path to a valid service account JSON key file.
    
        Returns:
            A service that is connected to the specified API.
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)
    
        # Build the service object.
        service = build(api_name, api_version, credentials=credentials)
    
        return service
    
    # Helper function to create a UUID for each request
    def generated_uui():
        return str(uuid.uuid4())
    
    def create_batch_request(callback):
        # For more info on supported regions
        # check: https://cloud.google.com/data-catalog/docs/concepts/regions
    
        region='us-datacatalog.googleapis.com'
    
        return BatchHttpRequest(batch_uri='https://{}/batch'.format(region), callback=callback)
    
    container = DataContainer()
    
    # Scope to set up the Discovery Service config.
    scope = 'https://www.googleapis.com/auth/cloud-platform'
    
    # Create service.
    service = get_service(
        api_name='datacatalog',
        api_version='v1',
        scopes=[scope],
        key_file_location=service_key_file_location)
    
    # Create the batch request config.
    batch = create_batch_request(container.callback)
    
    #-------------------------------------------------------------#
    # 1. Start by fetching a list of entries using search call
    #-------------------------------------------------------------#
    
    # Create the search request body.
    # This example searches for all BigQuery tables in a project.
    search_request_body = {
      'query': 'type=TABLE system=BIGQUERY',
      'scope': {'includeProjectIds': [project_id]}
    }
    
    # Generated a unique ID for the request.
    request_id = generated_uui()
    
    # Add the request to the batch client.
    batch.add(service.catalog().search(body=search_request_body), request_id=request_id)
    
    # Execute the batch request.
    batch.execute()
    
    # Uncomment to verify the full response from search.
    # print(container.data)
    
    response = container.data[request_id]
    
    results = response['results']
    
    first_table = results[0]
    
    # Verify that a first table is present.
    print(first_table)
    
    second_table = results[1]
    
    # Verify that a second table is present
    print(second_table)
    
    #-------------------------------------------------------------------#
    # 2. Send the batch request to attach tags over the entire result set
    #-------------------------------------------------------------------#
    
    # Create a new container
    container = DataContainer()
    
    # Create a new batch request
    batch = create_batch_request(container.callback)
    
    # Set the template name config
    template_name = 'projects/[MY_PROJECT_ID]/locations/[MY-LOCATION]/tagTemplates/[MY-TEMPLATE-NAME]'
    
    for result in results:
        # Generated a unique id for request.
        request_id = generated_uui()
    
        # Add the entry name as the tag parent.
        parent=result['relativeResourceName']
    
        # Create the tag request body.
        create_tag_request_body = {
          'template': template_name,
           # CHANGE for your template field values.
          'fields': {'etl_score': {'doubleValue': 0.5}}
        }
    
        # Add requests to the batch client.
        batch.add(service.projects().locations().
                  entryGroups().entries().tags().
                  create(body=create_tag_request_body,
                         parent=parent),
                  request_id=request_id)
    
    # Execute the batch request.
    
    # Since the Batch Client works with regions
    # If you receive [HttpError 400 errors]
    # 1. Verify the region you used to create the Batch client
    # 2. Verify the region where the Entry is located.
    # 3. verify the region of the parent tag template used by the tag.
    
    batch.execute()
    
    # Uncomment to verify the full response from tag creation.
    # print(container)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
