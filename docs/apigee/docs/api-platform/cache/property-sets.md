---
url: https://docs.cloud.google.com/apigee/docs/api-platform/cache/property-sets/
title: Using property sets \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:36.498082+00:00
---

# Using property sets  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/cache/property-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using property sets Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

A _property set_ is a custom collection of key/value pairs that store data. API proxies can retrieve this data when they execute.

## Why use property sets?

Typically, you use property sets to store non-expiring data that shouldn't be hard-coded in your API proxy logic. You can access property set data anywhere in a proxy where you can access [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables).

A common use case for property sets is to provide values that are associated with one environment or another. For example, you can create an environment-scoped property set with configuration values that are specific to proxies running in your test environment, and another set for your production environment.

For example:

  * The `prod-env.properties` property set contains the property `log-level=error`
  * The `test-env.properties` property set contains the property `log-level=debug`



Similarly, you might store environment-specific routing information:

  * The `test-env.properties` property set contains the property `db-url=mydomain.test.datasource.com`
  * The `prod-env.properties` property set contains the property `db-url=mydomain.prod.datasource.com`



## Property set scopes

You can scope a property set to an API proxy revision or environment when you create the property set. You cannot scope a property set to an organization.

The following table explains the behavior and administration of property sets with API proxy and organization scope:

Scope | Runtime behavior | Administration  
---|---|---  
API proxy | Properties are available only to the revision of the API proxy that contains the property set resource. No other API proxy or revision of the same proxy can access that particular property set. | Administrators can use the [ /resourcefiles](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest#rest-resource:-v1.organizations.environments.resourcefiles) Apigee API or the UI to create and edit property sets. Saving the API proxy in the UI will create a new revision, and the modified property set will be associated with that revision only.   
Environment | Properties are available to all revisions of all API proxies within that environment. API proxies within other environments cannot access that property set.  | Administrators can use the [ /resourcefiles](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest#rest-resource:-v1.organizations.environments.resourcefiles) Apigee API or the [UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#ui-env) to create, view, update, or delete environment-scoped property sets.   
  
## Property set limits

Apigee imposes limits on property sets, as described in [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits). In addition, property set files must use the same syntax as [Java properties files](https://en.wikipedia.org/wiki/.properties), with one exception: you cannot use curly braces `{}` in property set files.

## Create property set files

Typically, you store property set values as name/value pairs in a file. Property set files are [resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) of type `properties`.

Property set files support the same syntax as [Java properties files](https://en.wikipedia.org/wiki/.properties); for example, they can contain Unicode values and can use `#` or `!` characters as comment markers. Note this one exception: you cannot use curly braces `{}` in property set files.

You must add the suffix `.properties` to a property file name. For example: `myconfig.my_key.properties` is allowed, but `myconfig.my_key` is not allowed. 

The structure of a property set specification is: `property_set_name.property_name.properties` The property set name and property name cannot have dots in them. For example: `myconfig.my_key.properties` is allowed, but `myconfig.my.key.properties` and `my.config.my_key.properties` are not allowed. 

The following example shows a simple property set file that defines several properties:
    
    
    # myProps.properties file
    # General properties
    foo=bar
    baz=biff
    
    # Messages/notes/warnings
    message=This is a basic message.
    note_message=This is an important message.
    error_message=This is an error message.
    
    # Keys
    publickey=abc123
    privatekey=splitwithsoundman

After you create a property set file, you upload it to Apigee using either the UI or API.

##  Manage property sets using the UI 

Manage property sets scoped to an API proxy revision using the UI in the same way you manage other resources. For more information, see [Manage proxy-level resources using the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#ui).

**Note:**

  * You can create, update, or delete property sets scoped to an API proxy revision only if that revision has not been deployed. After an API proxy revision is deployed, it is immutable. 
  * You cannot manage property sets that are scoped to an organization using the UI. For more information, see Property set scopes. 



##  Manage property sets using the API 

Manage property sets scoped to an API proxy revision or environment using the API, as described in the following sections. 

###  Create property sets using the API 

The following sections describe how to create property sets scoped to an API proxy revision or environment using the API.

#### Create property sets scoped to an API proxy revision using the API

**Note:** You can add a property set scoped to an existing API proxy revision only if the revision has not been deployed. After an API proxy revision is deployed, it is immutable.

To create a property set that is scoped to an API proxy revision using the API:

  1. Create the property set file.
  2. Add the property set file to an [API proxy configuration bundle](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).
  3. Upload the bundle using the [Create API proxy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/create) or [Update API proxy revision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision) API.



#### Create property sets scoped to an environment using the API

To add a property set that is scoped to an environment using the API, create the property set file and then upload it to an environment in your organization by issuing a `POST` request to the following resource: `https://apigee.googleapis.com/v1/organizations/{org}/environments/{env}/resourcefiles`

Include the following information with your request:

  * Set the `name` query parameter to the name of the property set
  * Set the `type` query parameter to `properties`
  * Pass the contents of the property set file as `application/octet-stream` or `multipart/form-data`

**Note:** When importing a property set file using the API, you might need to `chmod` the file's permissions so that your development tool (such as `curl`) can upload it.

The following example imports a property set named `MyPropSet` from the `/Users/myhome/myprops.properties` file:
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles?name=MyPropSet&type=properties"
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: multipart/form-data" \
      -F file=@/Users/myhome/myprops.properties
      

`$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl).

The following provides an example of the response. 
    
    
    {
      "name": "MyPropSet",
      "type": "properties"
    }

For more information, see [Create resource file API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/create). 

###  View property sets using the API 

The following sections describe how to view property sets scoped to an environment using the API. 

#### View all property sets scoped to an environment using the API 

To view all property sets scoped to an environment using the API, issue a `GET` request to the following resource: `https://apigee.googleapis.com/v1/organizations/{org}/environments/{env}/resourcefiles/properties`

The following example lists all property sets in the test environment:
    
    
    curl -X GET "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/properties" \
      -H "Authorization: Bearer $TOKEN"
      

`$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl).

The following provides an example of the response. 
    
    
    {
      "resourceFile": [
        {
          "name": "MyPropSet",
          "type": "properties"
        }
      ]
    }

For more information, see [List environment resource files API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/listEnvironmentResources). 

#### View the contents of a property set scoped to an environment using the API 

To view the contents of a property set scoped to an environment using the API, issue a `GET` request to the following resource: `https://apigee.googleapis.com/v1/organizations/{org}/environments/{env}/resourcefiles/properties/name`

The following example displays the contents of the `MyPropSet` property set in the test environment:
    
    
    curl -X GET "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/properties/MyPropSet" \
      -H "Authorization: Bearer $TOKEN"
      

`$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl).

The following provides an example of the response. 
    
    
    # myProps.properties file
    # General properties
    foo=bar
    baz=biff
    
    # Messages/notes/warnings
    message=This is a basic message.
    note_message=This is an important message.
    error_message=This is an error message.
    
    # Keys
    publickey=abc123
    privatekey=splitwithsoundman

For more information, see [List environment resource files API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/listEnvironmentResources). 

###  Update property sets using the API 

The following sections describe how to update property sets scoped to an API proxy revision or environment using the API.

#### Update property sets scoped to an API proxy revision using the API

**Note:** You can update a property set scoped to an API proxy revision only if the revision has not been deployed. After an API proxy revision is deployed, it is immutable.

To update a property set that is scoped to an API proxy revision using the API:

  1. Update the property set file.
  2. Download the API proxy configuration bundle using the [Get API proxy revision API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/get) with the following options: 
     * Set the `format` query parameter to `bundle`
     * Set the `Accept` header to `application/zip`
  3. Add the property set file to the [API proxy configuration bundle](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).
  4. Upload the API proxy configuration bundle using the [Update API proxy revision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision) API.



#### Update property sets scoped to an environment using the API 

To update a property set that is scoped to an environment using the API, update the property set file and then upload it to an environment in your organization by issuing a `PUT` request to the following resource: `https://apigee.googleapis.com/v1/organizations/{org}/environments/{env}/resourcefiles/{type}/{name}`

Include the following information with your request:

  * Set {type} to `properties`
  * Set {name} to the name of the property set that you want to update
  * Pass the contents of the property set file as `application/octet-stream` or `multipart/form-data`

**Note:** When importing a property set file using the API, you might need to `chmod` the file's permissions so that your development tool (such as `curl`) can upload it.

The following example updates the `MyPropSet` property set using the contents of the `/Users/myhome/myprops-revised.properties` file: 
    
    
    curl -X PUT "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/properties/MyPropSet"
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: multipart/form-data" \
      -F file=@/Users/myhome/myprops-revised.properties
      

`$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl).

The following provides an example of the response. 
    
    
    {
      "name": "MyPropSet",
      "type": "properties"
    }

For more information, see [Update resource file API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/update). 

###  Delete property sets using the API 

The following sections describe how to delete property sets scoped to an API proxy revision or environment using the API.

#### Delete property sets scoped to an API proxy revision using the API

**Note:** You can delete a property set scoped to an API proxy revision if it has not been deployed. After an API proxy revision is deployed, it is immutable.

To delete a property set that is scoped to an API proxy revision using the API:

  1. Download the API proxy configuration bundle using the [Get API proxy revision API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/get) with the following options: 
     * Set the `format` query parameter to `bundle`
     * Set the `Accept` header to `application/zip`
  2. Delete the property set file from the [API proxy configuration bundle](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).
  3. Upload the API proxy configuration bundle using the [Update API proxy revision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision) API.



####  Delete property sets scoped to an environment using the API 

To delete a property set scoped to an environment using the API, issue a `DELETE` request to the following resource: `https://apigee.googleapis.com/v1/organizations/{org}/environments/{env}/resourcefiles/{type}/{name}`

Pass the following information with your request:

  * Set {type} to `properties`
  * Set {name} to the name of the property set that you want to delete



The following example deletes the `MyPropSet` property set:
    
    
    curl -X DELETE https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/properties/MyPropSet \
      -H "Authorization: Bearer $TOKEN"
      

`$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl).

The following provides an example of the response. 
    
    
    {
      "name": "MyPropSet",
      "type": "properties"
    }

For more information, see [Delete resource file API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/delete). 

## Access property set values

Access property set values anywhere in an API proxy where you can access [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables): in policies, flows, JavaScript code, and so on.

To access values in a property set, use the following syntax:
    
    
    propertyset.[property_set_name].[property_name]

Where:

  * property_set_name is the filename that you defined (if you used the UI) or the value of the `name` query parameter (if you used the API).
  * property_name is the name of the property. For example, if your property set contains `foo=bar`, `foo` is the name of the property and `bar` is the value.



For example, in a [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy), use the `getVariable()` method to get a value from a property set:
    
    
    context.getVariable('propertyset.property_set_name.property_name);

The following example gets the value of the `foo` property in the property set named "MyPropSet":
    
    
    context.getVariable('propertyset.MyPropSet.foo);

You can also use the [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) to get the value of a property from a property set and assign it to another variable, as the following example shows:
    
    
    <ExtractVariables name="ExtractVariables-1">
       <DisplayName>Extract a portion of the url path</DisplayName>
       <Source>request</Source>
       <Variable name="propertyset.MyPropSet.foo">
          <Pattern>{myVar}</Pattern>
       </Variable>
       <VariablePrefix>foobar</VariablePrefix>
       <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

In this example, the policy reads the variable from the attribute `name`, and assigns the value to the variable in the `Pattern` element. 

##  Assign the value of a property set key dynamically using the Assign Message policy 

You can use the Assign Message policy to assign the value of property set key to a flow variable dynamically. For details, see the [PropertySetRef](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable-propset) description in the Assign Message policy reference. 

##  For Apigee hybrid users 

If you are using Apigee hybrid, note the following: 

  1. The hybrid management plane validates the property set; if valid, the properties are stored in the management plane.
  2. The Synchronizer retrieves the property set data and stores it locally on the runtime plane.
  3. The Message Processor loads the downloaded property set and makes it available to executing proxies.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
