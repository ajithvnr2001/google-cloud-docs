---
url: https://docs.cloud.google.com/bigtable/docs/samples-nodejs-hello/
title: Node.js hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:16.216796+00:00
---

# Node.js hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-nodejs-hello/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Node.js hello world

This code sample is a "hello world" application that runs on Node.js. The sample illustrates how to complete the following tasks:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.



## Set up authentication

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

## Running the sample

This code sample uses the [Bigtable package](https://github.com/googleapis/nodejs-bigtable) of the [Google Cloud Client Library for Node.js](https://github.com/googleapis/google-cloud-node) to communicate with Bigtable.

To run this sample program, follow the [instructions for the sample on GitHub](https://github.com/googleapis/nodejs-bigtable/tree/master/samples/hello-world).

## Using the Cloud Client Library with Bigtable

The sample application connects to Bigtable and demonstrates some simple operations.

### Requiring the client library

The sample requires the `@google-cloud/bigtable` module, which provides the [`Bigtable`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Bigtable) class.
    
    
    const {Bigtable} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)');

### Connecting to Bigtable

To connect to Bigtable, create a new [`Bigtable`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Bigtable) object. Then call its [`instance()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Bigtable#instance) method to get an [`Instance`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Instance) object that represents your Bigtable instance.
    
    
    const bigtableClient = new Bigtable();
    const instance = bigtableClient.instance(INSTANCE_ID);
    const table = instance.table(TABLE_ID);

### Creating a table

Call the instance's [`table()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Instance#table) method to get a [`Table`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Table) object that represents the table for "hello world" greetings. If the table doesn't exist, call the table's [`create()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Table#create) method to create a table with a single column family that retains one version of each value.

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
    const {BigtableTableAdminClient} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)').v2;
    const adminClient = new [BigtableTableAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)();
    const projectId = await adminClient.getProjectId();
    
    let tableExists = true;
    try {
      await adminClient.getTable({
        name: `projects/${projectId}/instances/${INSTANCE_ID}/tables/${TABLE_ID}`,
      });
    } catch (e) {
      if (e.code === 5) {
        tableExists = false;
      }
    }
    if (!tableExists) {
      console.log(`Creating table ${TABLE_ID}`);
      const {BigtableTableAdminClient} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)').v2;
      const adminClient = new [BigtableTableAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)();
      const projectId = await adminClient.getProjectId();
      await adminClient.createTable({
        parent: `projects/${projectId}/instances/${INSTANCE_ID}`,
        tableId: TABLE_ID,
        table: {
          columnFamilies: {
            [COLUMN_FAMILY_ID]: {
              gcRule: {
                maxNumVersions: 1,
              },
            },
          },
        },
      });
    }

### Writing rows to a table

Use an array of greeting strings to create some new rows for the table: call the array's `map()` method to create a new array of objects that represent rows, then call the table's [`insert()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Table#insert) method to add the rows to the table.
    
    
    console.log('Write some greetings to the table');
    const greetings = ['Hello World!', 'Hello Bigtable!', 'Hello Node!'];
    const rowsToInsert = greetings.map((greeting, index) => ({
      // Note: This example uses sequential numeric IDs for simplicity, but this
      // pattern can result in poor performance in a production application.
      // Rows are stored in sorted order by key, so sequential keys can result
      // in poor distribution of operations across nodes.
      //
      // For more information about how to design an effective schema for Cloud
      // Bigtable, see the documentation:
      // https://cloud.google.com/bigtable/docs/schema-design
      key: `greeting${index}`,
      data: {
        [COLUMN_FAMILY_ID]: {
          [COLUMN_QUALIFIER]: {
            // Setting the timestamp allows the client to perform retries. If
            // server-side time is used, retries may cause multiple cells to
            // be generated.
            timestamp: new Date(),
            value: greeting,
          },
        },
      },
    }));
    await table.insert(rowsToInsert);

### Creating a filter

Before you read the data that you wrote, create a filter to limit the data that Bigtable returns. This filter tells Bigtable to return only the most recent cell for each column, even if the column contains older cells.
    
    
    const filter = [
      {
        column: {
          cellLimit: 1, // Only retrieve the most recent version of the cell.
        },
      },
    ];

### Reading a row by its row key

Call the table's [`row()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Table#row) method to get a reference to the row with a specific row key. Then call the row's [`get()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Row#get) method, passing in the filter, to get one version of each value in that row.
    
    
    console.log('Reading a single row by row key');
    const [singleRow] = await table.row('greeting0').get({filter});
    console.log(`\tRead: ${getRowGreeting(singleRow)}`);

### Scanning all table rows

Call the table's [`getRows()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Table#getRows) method, passing in the filter, to get all of the rows in the table. Because you passed in the filter, Bigtable returns only one version of each value.
    
    
    console.log('Reading the entire table');
    // Note: For improved performance in production applications, call
    // `Table#readStream` to get a stream of rows. See the API documentation:
    // https://cloud.google.com/nodejs/docs/reference/bigtable/latest/Table#createReadStream
    const [allRows] = await table.getRows({filter});
    for (const row of allRows) {
      console.log(`\tRead: ${getRowGreeting(row)}`);
    }

### Deleting a table

Delete the table with the table's [`delete()`](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/Table#delete) method.
    
    
    console.log('Delete the table');
    const request = {
      name: `projects/${projectId}/instances/${INSTANCE_ID}/tables/${TABLE_ID}`,
    };
    await adminClient.deleteTable(request);

## Putting it all together

Here is the full code sample without comments.
    
    
    
    
    const {Bigtable} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)');
    
    const TABLE_ID = 'Hello-Bigtable';
    const COLUMN_FAMILY_ID = 'cf1';
    const COLUMN_QUALIFIER = 'greeting';
    const INSTANCE_ID = process.env.INSTANCE_ID;
    
    if (!INSTANCE_ID) {
      throw new Error('Environment variables for INSTANCE_ID must be set!');
    }
    
    const getRowGreeting = row => {
      return row.data[COLUMN_FAMILY_ID][COLUMN_QUALIFIER][0].value;
    };
    
    (async () => {
      try {
        const bigtableClient = new Bigtable();
        const instance = bigtableClient.instance(INSTANCE_ID);
        const table = instance.table(TABLE_ID);
    
        const {BigtableTableAdminClient} = require('@google-cloud/bigtable').v2;
        const adminClient = new BigtableTableAdminClient();
        const projectId = await adminClient.getProjectId();
    
        let tableExists = true;
        try {
          await adminClient.getTable({
            name: `projects/${projectId}/instances/${INSTANCE_ID}/tables/${TABLE_ID}`,
          });
        } catch (e) {
          if (e.code === 5) {
            tableExists = false;
          }
        }
        if (!tableExists) {
          console.log(`Creating table ${TABLE_ID}`);
          const {BigtableTableAdminClient} = require('@google-cloud/bigtable').v2;
          const adminClient = new BigtableTableAdminClient();
          const projectId = await adminClient.getProjectId();
          await adminClient.createTable({
            parent: `projects/${projectId}/instances/${INSTANCE_ID}`,
            tableId: TABLE_ID,
            table: {
              columnFamilies: {
                [COLUMN_FAMILY_ID]: {
                  gcRule: {
                    maxNumVersions: 1,
                  },
                },
              },
            },
          });
        }
    
        console.log('Write some greetings to the table');
        const greetings = ['Hello World!', 'Hello Bigtable!', 'Hello Node!'];
        const rowsToInsert = greetings.map((greeting, index) => ({
          key: `greeting${index}`,
          data: {
            [COLUMN_FAMILY_ID]: {
              [COLUMN_QUALIFIER]: {
                timestamp: new Date(),
                value: greeting,
              },
            },
          },
        }));
        await table.insert(rowsToInsert);
    
        const filter = [
          {
            column: {
              cellLimit: 1, // Only retrieve the most recent version of the cell.
            },
          },
        ];
    
        console.log('Reading a single row by row key');
        const [singleRow] = await table.row('greeting0').get({filter});
        console.log(`\tRead: ${getRowGreeting(singleRow)}`);
    
        console.log('Reading the entire table');
        const [allRows] = await table.getRows({filter});
        for (const row of allRows) {
          console.log(`\tRead: ${getRowGreeting(row)}`);
        }
    
        console.log('Delete the table');
        const request = {
          name: `projects/${projectId}/instances/${INSTANCE_ID}/tables/${TABLE_ID}`,
        };
        await adminClient.deleteTable(request);
      } catch (error) {
        console.error('Something went wrong:', error);
      }
    })();

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
