---
url: https://docs.cloud.google.com/appengine/docs/flexible/configuring-datastore-indexes-with-index-yaml/
title: Configure Datastore indexes with index.yaml \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:10.604324+00:00
---

# Configure Datastore indexes with index.yaml  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/configuring-datastore-indexes-with-index-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/flexible/apis)



Send feedback 

#  Configure Datastore indexes with index.yaml Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

You can use [Firestore in Datastore mode (Datastore)](https://docs.cloud.google.com/appengine/docs/flexible/using-firestore-in-datastore-mode) for storing data for your applications that run in the flexible environment. Datastore uses [indexes](https://docs.cloud.google.com/datastore/docs/concepts/indexes) for every query your application makes. These indexes are updated whenever an entity changes, so the results can be returned quickly when the app makes a query. To do this, Datastore needs to know in advance which queries the application will make. You specify which indexes your app needs in a `index.yaml` configuration file. You can use the Datastore emulator to generate the file automatically as you test your app, or write the file yourself. The `index.yaml` file must be uploaded when you deploy your app.

## Sample `index.yaml`

Every Datastore query made by an application needs a corresponding index. Indexes for simple queries, such as queries over a single property, are created automatically. Indexes for complex queries must be defined in a configuration file named `index.yaml`. This file is uploaded with the application to create indexes in Datastore.

The following is an example of an `index.yaml` file:
    
    
    indexes:
    
    - kind: Cat
      ancestor: no
      properties:
      - name: name
      - name: age
        direction: desc
    
    - kind: Cat
      properties:
      - name: name
        direction: asc
      - name: whiskers
        direction: desc
    
    - kind: Store
      ancestor: yes
      properties:
      - name: business
        direction: asc
      - name: owner
        direction: asc
    

The syntax of `index.yaml` is the YAML format. For more information about this syntax, see [the YAML website](http://www.yaml.org/) for more information.

**Note:** The YAML format supports comments. A line that begins with a pound (`#`) character is ignored:  
`# This is a comment.`

## Index definitions

`index.yaml` has a single list element called `indexes`. Each element in the list represents an index for the application.

An index element can have the following elements:

`kind`
    Required. The kind of the entity for the query.
`properties`
    

A list of properties to include as columns of the index, in the order to be sorted: properties used in equality filters first, followed by the property used in inequality filters, then the sort orders and their directions.

Each element in this list has the following elements:

`name`
    The datastore name of the property.
`direction`
    The direction to sort, either `asc` for ascending or `desc` for descending. This is only required for properties used in sort orders of the query, and must match the direction used by the query. The default is `asc`.

`ancestor`
     `yes` if the query has an ancestor clause (either [Query.ancestor()](https://docs.cloud.google.com/appengine/docs/standard/python/datastore/queryclass#Query_ancestor) or a GQL [ANCESTOR IS](https://docs.cloud.google.com/appengine/docs/standard/python/datastore/gqlreference) clause). The default is `no`. 

## Create index files

You can create an index file manually, using a text editor and following the file layout described above. A more efficient approach is to automatically generate the file as you test your app locally. You can combine the two methods.

When you are testing in your local environment, you can use the [gcloud emulator command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/start) to start a service that emulates Datastore before you run your app:
    
    
    gcloud beta emulators datastore start --data-dir DATA-DIR
    

Use the `--data-dir` flag to specify the directory where the auto-generated `index.yaml` file will appear.

As you test your app, each time you generate a Datastore query, the emulator adds a generated index definition to `index.yaml`. All the automatically generated index definitions will appear in the file below the following line:
    
    
    # AUTOGENERATED
    

All index definitions above this line are considered to be under manual control, and are not updated by the development web server. The web server will only make changes below the line, and will only do so if the complete `index.yaml` file does not describe an index that accounts for a query executed by the application. To take control of an automatic index definition, move it above this line.

The emulator may update existing definitions below this line as the application makes queries. If the app generates every query it will make while you test it, then the generated entries in `index.yaml` will be complete. You might need to edit the file manually to delete indexes that are not used in production, or to define indexes that were not created while testing.

## Deploy the index configuration file

To deploy the `index.yaml` configuration file, run the following command:
    
    
    gcloud app deploy index.yaml
    

## Delete unused indexes

When you change or remove an index from the index configuration, the original index is not deleted from App Engine automatically. This gives you the opportunity to leave an older version of the app running while new indexes are being built, or to revert to the older version immediately if a problem is discovered with a newer version.

When you are sure that old indexes are no longer needed, you can delete them from App Engine as follows:
    
    
    gcloud datastore indexes cleanup index.yaml
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
