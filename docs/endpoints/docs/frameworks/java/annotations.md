---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations/
title: Cloud Endpoints Frameworks annotations and syntax \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:40.997290+00:00
---

# Cloud Endpoints Frameworks annotations and syntax  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Cloud Endpoints Frameworks annotations and syntax Stay organized with collections  Save and categorize content based on your preferences. 

The Endpoints Frameworks annotations describe API configuration, methods, parameters, and other vital details that define the properties and behavior of the endpoint.

See [Writing and annotating code](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code) for information on adding annotations by using a Maven project. Maven App Engine Cloud Endpoints artifacts are provided to create and build a backend API, and generate a client library from it.

The annotation that specifies configuration and behavior across the entire API (affecting all the classes exposed in the API and all their exposed methods) is `@Api`. _All public, non-static, non-bridge methods of a class annotated with`@Api` are exposed in the public API._

If you need special API configuration for a particular method, you can optionally use `@ApiMethod` to set configuration on a per-method basis. You configure these annotations by setting various attributes, as shown in the following tables.

**Note:** The Javadoc lists some annotations that are currently not implemented. These annotations are: [`ApiCacheControl`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiCacheControl), and [`ApiFrontendLimits`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits).

## `@Api`: API-scoped annotations

The annotation [`@Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api) configures the whole API, and applies to all public methods of a class unless overridden by `@ApiMethod`.

**Important:** If you implement your API from multiple classes, see [Multiclass APIs](https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass).

To override a given `@Api` annotation for a specific class within an API, see `@ApiClass` and `@ApiReference`.

### Required imports

To use this feature, you need the following import:
    
    
    import com.google.api.server.spi.config.Api;
    

### Attributes

@Api Attributes | Description | Example  
---|---|---  
`audiences` | Required if your API requires authentication and if you are supporting Android clients. For more information, see Client IDs and audiences. | `audiences = {"1-web-apps.apps.googleusercontent.com", "2-web-apps.apps.googleusercontent.com"}`  
`apiKeyRequired` | Optional. Used to restrict access to requests that supply an [API key](https://docs.cloud.google.com/endpoints/docs/frameworks/java/restricting-api-access-with-api-keys-frameworks). | `apiKeyRequired = AnnotationBoolean.TRUE`  
`authenticators` | Required if your API authenticates using Firebase, Auth0, or service accounts. This attribute isn't required if your API authenticates using [Google ID tokens](https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users#google-id-tokens). You can set this at the API level or at the individual method level. Set it to `{EspAuthenticator.class}`, or you can write your own custom authenticator, as described in [Interface Authenticator](https://cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator). | `authenticators = {EspAuthenticator.class}`  
`backendRoot` | Deprecated. To serve your API from a different path, in your `web.xml` file, change the `url-pattern` in the `EndpointsServlet` section. | `<url-pattern>/example-api/*</url-pattern>`  
`canonicalName` | Used to specify a different or more readable name for the API _in the client library_. This name is used to generate the names in the client library; the backend API continues to use the value specified in the `name` property.For example, if your API has the `name` set to **dfaanalytics** , you could use this property to specify a canonical name of **DFA Group Analytics** ; the generated client classes would then contain the name `DfaGroupAnalytics`.You should include the relevant spaces between the names; these are replaced by the appropriate camel casing or underscores. | `canonicalName = "DFA Analytics:"`n  
`clientIds` | Required if your API uses authentication. List of client IDs for clients allowed to request tokens. For more information, see Client IDs and audiences. | `clientIds = {"1-web-apps.apps.googleusercontent.com", "2-android-apps.apps.googleusercontent.com"}`  
`defaultVersion` | Specifies whether a default version is used if none is supplied in the `version` attribute. | `defaultVersion = AnnotationBoolean.TRUE`  
`description` | A short description of the API. This is exposed in the discovery service to describe your API, and may optionally also be used to generate documentation. | `description = "Sample API for a simple game"`  
`documentationLink` | The URL where users can find documentation about this version of the API. This is surfaced in the API Explorer "Learn More" highlight at the top of the API Explorer page to allow users to learn about your service. | `documentationLink = "http://link_to/docs"`  
`issuers` | The custom JWT issuer configurations. | `issuers = { @ApiIssuer(name = "auth0", issuer = "https://test.auth0.com/authorize", jwksUri = "https://test.auth0.com/.well-known/jwks.json") }`  
`issuerAudiences` | Audiences for individual issuers. | `issuerAudiences = { @ApiIssuerAudience(name = "auth0", audiences = {"aud-1.auth0.com", "aud-2.auth0.com"}) }`  
`limitDefinitions` | Optional. Used to define [quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-overview) for your API. See `@ApiLimitMetric`. | `limitDefinitions = { @ApiLimitMetric(name = "read-requests", displayName = "Read requests", limit = 1000)}`  
`name` | The name of the API, which is used as the prefix for all of the API's methods and paths. The `name` value:

  * _Must_ begin with lowercase
  *  _Must_ match the regular expression `[a-z]+[A-Za-z0-9]*`

If you don't specify `name`, the default `myapi` is used. | `name = "foosBall"`  
`namespace` | Configures namespacing for generated clients. See `@ApiNamespace`. | `namespace=@ApiNamespace(ownerDomain="your-company.com", ownerName="YourCo", packagePath="cloud/platform"`)  
`root` | Deprecated. To serve your API from a different path, in your `web.xml` file, change the `url-pattern` in the `EndpointsServlet` section. | `<url-pattern>/example-api/*</url-pattern>`  
`scopes` | If not supplied, the default is the email scope (`https://www.googleapis.com/auth/userinfo.email`), which is required for OAuth. You can override this to specify more [OAuth 2.0 scopes](https://docs.cloud.google.com/accounts/docs/OAuth2) if you wish. However, if you do define more than one scope, note that the scope check passes if the token is minted for _any_ of the specified scopes. To require multiple scopes, a single `String` should be specified with a space between each scope. To override the scopes specified here for a particular API method, specify different scopes in the `@ApiMethod` annotation. | `scopes = {"ss0", "ss1 and_ss2"}`  
`title` | The text displayed in API Explorer as the title of your API, and exposed in the discovery and the directory services. | `title = "My Backend API"`  
`transformers` | Specifies a list of custom transformers. Note that there is an alternative annotation (`@ApiTransformer`) that is preferable. This attribute is overridden by `@ApiTransformer`. | `transformers = {BazTransformer.class}`  
`version` | Specifies your version of endpoint. If you don't supply this, the default `v1` is used. | `version = "v2"`  
  
### Sample`@Api` annotation

This annotation is placed before the class definition:
    
    
    /** An endpoint class we are exposing. */
    @Api(name = "myApi",
        version = "v1",
        namespace = @ApiNamespace(ownerDomain = "helloworld.example.com",
            ownerName = "helloworld.example.com",
            packagePath = ""))

### Client IDs and audiences

For OAuth2 authentication, an OAuth2 token is issued to a specific client ID, which means that you can use the client ID to restrict access to your APIs. When you register an Android application in the Google Cloud console, you create a client ID for it. This client ID is the one requesting an OAuth2 token from Google for authentication purposes. When the backend API is protected by auth, an OAuth2 access token is sent and opened by Endpoints, the client ID is extracted from the token, and then the ID is compared to the backend's declared acceptable client ID list (the `clientIds` list).

If you want your Endpoints API to authenticate callers, you need to supply a list of `clientIds` that are allowed to request tokens. This list should consist of the all client IDs you have obtained through the [Google Cloud console](https://console.cloud.google.com/) for your web or Android clients. This means that the clients must be known at API build-time. If you specify an empty list, `{}`, then no clients can access the methods protected by Auth.

If you use the `clientIds` attribute and you want to test authenticated calls to your API using the Google API Explorer, you must supply its client ID in the list of `clientIds`: the value to use is `com.google.api.server.spi.Constant.API_EXPLORER_CLIENT_ID`.

**Note:** If you don't use the `clientIds` attribute, you don't need to supply the API Explorer client ID.

#### About audiences

The `clientIds` list _protects the backend API_ from unauthorized clients. But further protection is needed to _protect the clients_ , so that their auth token only works for the intended backend API. For Android clients, this mechanism is the `audiences` attribute, in which you specify the client ID of the backend API.

Note that when you create a Google Cloud console project, a default client ID is automatically created and named for use by the project. When you upload your backend API into App Engine, it uses that client ID. This is the web client ID mentioned in [API authentication](https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users).

## `@ApiMethod`: Method-scoped annotations

The annotation [`@ApiMethod`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod) is used to supply a different API configuration than the defaults provided by the `@Api` or `@ApiClass` annotations. Note that this is optional: all public, non-static, and non-bridge methods in a class with an `@Api` annotation are exposed in the API, whether they have an `@ApiMethod` annotation or not.

Attributes within this annotation allow you to configure details of a single API method. If the same attribute is specified in `@Api` and `@ApiMethod`, `@ApiMethod` overrides.

**Important:** Certain query parameters are reserved and cannot be used in an API method. For a list of these, see [Standard query parameters](https://developers.google.com/drive/web/query-parameters)

### Required imports

To use this feature, you need the following imports:
    
    
    import com.google.api.server.spi.config.AnnotationBoolean;
    import com.google.api.server.spi.config.ApiMethod;
    import com.google.api.server.spi.config.ApiMethod.HttpMethod;
    

### Attributes

@ApiMethod Attributes | Description | Example  
---|---|---  
`apiKeyRequired` | Optional. Used to restrict access to requests that supply an [Api key](https://docs.cloud.google.com/endpoints/docs/frameworks/java/restricting-api-access-with-api-keys-frameworks). | `apiKeyRequired = AnnotationBoolean.TRUE`  
`audiences` | Supply this if you wish to override the configuration in `@API`. For more information, see Client IDs and audiences. | `audiences = {"1-web-apps.apps.googleusercontent.com", "2-web-apps.apps.googleusercontent.com"}`  
`authenticators` | Required if your API authenticates by using Firebase, Auth0, or service accounts, and you haven't set this attribute at the API level. This attribute isn't required if your API authenticates using [Google ID tokens](https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users#authenticating_with_google_id_tokens). Set it to `{EspAuthenticator.class}`, or you can write your own custom authenticator, as described in [Interface Authenticator](https://cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator) | `authenticators = {EspAuthenticator.class}`  
`clientIds` | List of client IDs for clients allowed to request tokens. Required if your API uses authentication. | `clientIds = {"1-web-apps.apps.googleusercontent.com", "2-android-apps.apps.googleusercontent.com"}`  
`httpMethod` | The HTTP method to use. If you don't set this, a default is chosen based on the name of the method. | `httpMethod = HttpMethod.GET`  
`issuerAudiences` | Supply this if you wish to override the configuration in `@Api`. | `issuerAudiences = { @ApiIssuerAudience(name = "auth0", audiences = {"aud-1.auth0.com", "aud-2.auth0.com"}) }`  
`metricCosts` | Optional. Indicates that the method has a quota limit. You assign the `@ApiMetricCost` annotation to `metricCosts`. You must also specify the `limitDefinitions` attribute to define the quota in the `@Api` annotation. The `@ApiMetricCost`annotation takes the following attributes:

  * **name:** A name that you specified in the ApiLimitMetric annotation.
  * **cost:** An integer that specifies the cost for each request. The cost allows methods to consume at different rates from the same quota. For example, if a quota has a limit of 1000 and a cost of 1, the calling application can make 1000 requests per minute before going over the limit. With a cost of 2 for the same quota, a calling application can make only 500 requests per minute before going over the limit.

| `metricCosts = { @ApiMetricCost(name = read-requests", cost = 1) }`  
`name` | The name for this method in the generated client library. This is automatically prefixed with your API name to create a unique name for the method. The `name` value:

  * _Must_ begin with lowercase
  *  _Must_ match the regular expression `[a-z]+[A-Za-z0-9]*`

If you don't specify `name`, the default `myapi` is used. | `name = "foosBall.list"`  
`path` | The URI path to use to access this method. If you don't set this, a default path is used based on the Java method name. If you plan to [add API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management), don't include a trailing slash in the path. | `path = "foos"`  
`scopes` | Specify one or more OAuth 2.0 scopes, one of which is required for calling this method. If you set `scopes` for a method, it overrides the setting in the `@Api` annotation. If you do define more than one scope, note that the scope check passes if the token is minted for _any_ of the specified scopes. To require multiple scopes, specify a single `String` with a space between each scope. | `scopes = {"ss0", "ss1 and_ss2"}`  
  
### Sample `@ApiMethod` annotation

This annotation is placed before the method definition inside a class:
    
    
    /** A simple endpoint method that takes a name and says Hi back. */
    @ApiMethod(
        name = "sayHiUser",
        httpMethod = ApiMethod.HttpMethod.GET)
    public MyBean sayHiUser(@Named("name") String name, User user)
        throws OAuthRequestException, IOException {
      MyBean response = new MyBean();
      response.setData("Hi, " + name + "(" + user.getEmail() + ")");
    
      return response;
    }

Methods that take an entity as a parameter should use `HttpMethod.POST` (for insert operations) or `HttpMethod.PUT` (for update operations):
    
    
    @ApiMethod(
        name = "mybean.insert",
        path = "mybean",
        httpMethod = ApiMethod.HttpMethod.POST
    )
    public void insertFoo(MyBean foo) {
    }

## `@Named`

The `@Named` annotation is required for all non-entity type parameters passed to server-side methods. This annotation indicates the name of the parameter in the request that gets injected here. A parameter that isn't annotated with `@Named` is injected with the whole request object.

**Important:** There are several commonly used `@Named` annotations: the ones you can use with Endpoints Frameworks are `javax.inject.Named` or `com.google.api.server.spi.config.Named`.

### Required imports

To use this feature, you need the following imports:
    
    
    import javax.inject.Named;
    

This sample shows the use of `@Named`:
    
    
    /** A simple endpoint method that takes a name and says Hi back. */
    @ApiMethod(name = "sayHi")
    public MyBean sayHi(@Named("name") String name) {
      MyBean response = new MyBean();
      response.setData("Hi, " + name);
    
      return response;
    }

where `@Named` specifies that only the `id` parameter is injected in the request.

## `@ApiLimitMetric`

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section describes the annotations required to define [quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-overview) for your API. See [Configuring quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-configure) for all the steps required to setup a quota.

You assign the `@ApiLimitMetric` annotation to the `limitDefinitions` attribute of the API-scoped annotations. You must also add `@ApiMetricCost` to the `@ApiMethod` annotations for each method that you want to apply a quota to.

### Required imports

To use this feature, you need the following import:
    
    
    import com.google.api.server.spi.config.ApiLimitMetric;
    

### Attributes

`@ApiLimitMetric` attributes  | Description  
---|---  
name | The name for the quota. Typically, this is the type of request (for example, "read-requests" or "write-requests") that uniquely identifies the quota  
displayName | The text displayed to identify the quota on the **Quotas** tab on **Endpoints** > **Services** page of the Google Cloud console. This text is also displayed to consumers of your API on the **Quotas** page of IAM & admin and API & services. The display name must be a maximum of 40 characters.  
For readability purposes, the text "per minute per project" is automatically appended to the display name on the **Quotas** pages.   
To maintain consistency with the display names of Google services listed on the **Quotas** pages that consumers of your API see, we recommend the following for the display name:  


  * Use "Requests" when you only have one metric.
  * When you have multiple metrics, each should describe the type of request and contain the word "requests" (for example "Read requests" or "Write requests"). 
  * Use "quota units" instead of "requests" when any of the costs for this quota is greater than 1.

  
limit | An integer value that is the maximum number of requests per minute per consumer project for the quota.  
  
### Example
    
    
    limitDefinitions = {
          @ApiLimitMetric(
            name = "read-requests",
            displayName = "Read requests",
            limit = 1000),
          @ApiLimitMetric(
            name = "write-requests",
            displayName = "Write requests",
            limit = 50),
        }
    

## `@ApiNamespace`

The [`@ApiNamespace`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace) annotation causes the generated client libraries to have the namespace you specify, rather than a default constructed during client library generation.

By default, if you don't use this annotation, the namespace that is used is the reverse of `your-project-id.appspot.com`. That is, the package path is `com.appspot.your-project-id.yourApi`.

You can change the default namespace by supplying the `@ApiNamespace` annotation within the `@Api` annotation:
    
    
    /** An endpoint class we are exposing. */
    @Api(name = "myApi",
        version = "v1",
        namespace = @ApiNamespace(ownerDomain = "helloworld.example.com",
            ownerName = "helloworld.example.com",
            packagePath = ""))

Set the `ownerDomain` attribute to your own company domain and `ownerName` to your company name, for example, `your-company.com`. The reverse of the `ownerDomain` is used for the package path: `com.your-company.yourApi`.

You can optionally use the `packagePath` attribute to provide further scoping. For example, by setting `packagePath` to `cloud`, the package path used in the client library is `com.your-company.cloud.yourApi`. You can add more values to the package path by supplying the delimiter `/`: `packagePath="cloud/platform"`.

## `@Nullable`

This annotation indicates that a parameter of a method is optional (and therefore a query parameter). `@Nullable` may only be used with `@Named` parameters.

## `@ApiClass`

In a [multiclass API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass), you can use `@ApiClass`to specify different properties for a given class, overriding equivalent properties in the `@Api` configuration. See [Using `@ApiClass` for properties that can differ between classes](https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass#using_apiclass_for_properties_that_can_differ_between_classes) for a complete description of this annotation.

## `@ApiReference`

In a [multiclass API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass), you can use `@ApiReference` to supply an alternate method of annotation inheritance. See [Using `@ApiReference` inheritance](https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass#using_apireference_inheritance) for a complete description of this annotation.

## `@ApiResourceProperty`

[`@ApiResourceProperty`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiResourceProperty) provides control over how resource properties are exposed in the API. You can use it on a property getter or setter to omit the property from an API resource. You can also use it on the field itself, if the field is private, to expose it in the API. You can also use this annotation to change the name of a property in an API resource.

### Required imports

To use this feature, you need the following imports:
    
    
    import com.google.api.server.spi.config.ApiResourceProperty;
    import com.google.api.server.spi.config.AnnotationBoolean;
    

### Attributes

@ApiResourceProperty Attributes | Description | Example  
---|---|---  
`ignored` | If set to `AnnotationBoolean.TRUE`, omits the property. If not specified or set to `AnnotationBoolean.FALSE`, the property is not omitted. | `@ApiResourceProperty(ignored = AnnotationBoolean.TRUE)`  
`name` | If supplied, it specifies the property name to be exposed in the API. | `@ApiResourceProperty(name = "baz")`  
  
### Sample class with `@ApiResourceProperty`

The following snippet shows a class with property getters annotated with `@ApiResourceProperty`:
    
    
    class Resp {
      private String foobar = "foobar";
      private String bin = "bin";
    
      @ApiResourceProperty
      private String visible = "nothidden";
    
      @ApiResourceProperty(ignored = AnnotationBoolean.TRUE)
      public String getBin() {
        return bin;
      }
    
      public void setBin(String bin) {
        this.bin = bin;
      }
    
      @ApiResourceProperty(name = "baz")
      public String getFoobar() {
        return foobar;
      }
    
      public void setFoobar(String foobar) {
        this.foobar = foobar;
      }
    }
    
    public Resp getResp() {
      return new Resp();
    }
    

In the preceding code snippet, `@ApiResourceProperty` is applied to the `getBin` getter for the `bin` property, with the `ignored` attribute setting telling Endpoints Frameworks to omit this property in the API resource.

`@ApiResourceProperty` is also applied to the private field `visible`, which has no getter or setter. Using this annotation exposes this field as a property in the API resource.

In the same snippet, `@ApiResourceProperty` is also applied to a different getter, `getFoobar`, which returns a property value for the `foobar` property. The `name` attribute in this annotation tells Endpoints Frameworks to change the property name in the API resource. The property value itself is unchanged.

In the preceding example snippet, the JSON representation of a `Resp` object looks similar to this:
    
    
    {"baz": "foobar", "visible": "nothidden"}
    

## `@ApiTransformer`

The [`@ApiTransformer`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiTransformer) annotation customizes how a type is exposed in Endpoints through transformation to and from another type. (The transformer specified must be an implementation of `com.google.api.server.spi.config.Transformer`.)

Using the `@ApiTransformer` annotation on a class is the preferred way to specify a transformer. However, you can alternatively specify your custom transformer in the `transformer` attribute of the `@Api` annotation.

**Note:** Using `@ApiTransformer` is preferred to specifying transformers on an `@Api` annotation. If your app consists of multiple APIs, the transformer specified in `@ApiTransformer` works for all of them, whereas using `@Api` to specify the transformer requires you to repeat this specification in each API.

### Required imports

To use this feature, you need the following import:
    
    
    import com.google.api.server.spi.config.ApiTransformer;
    

### Sample class with `@ApiTransformer`

The following snippet shows a class annotated with `@ApiTransformer`:
    
    
    @ApiTransformer(BarTransformer.class)
    public class Bar {
      private final int x;
      private final int y;
    
      public Bar(int x, int y) {
        this.x = x;
        this.y = y;
      }
    
      public int getX() {
        return x;
      }
    
      public int getY() {
        return y;
      }
    }
    

This class is transformed by the `BarTransformer` class.

### Sample Endpoints transformer class

The following snippet shows a sample transformer class named `BarTransformer`. This is the transformer referenced by `@ApiTransformer` in the preceding snippet:
    
    
    public class BarTransformer implements Transformer<Bar, String> {
      public String transformTo(Bar in) {
        return in.getX() + "," + in.getY();
      }
    
      public Bar transformFrom(String in) {
        String[] xy = in.split(",");
        return new Bar(Integer.parseInt(xy[0]), Integer.parseInt(xy[1]));
      }
    }

Assuming there is an object with a property `bar` of type `Bar`, without the preceding transformer, the object is represented as:
    
    
    {"bar": {"x": 1, "y": 2}}
    

With the transformer, the object is represented as:
    
    
    {"bar": "1,2"}
    

**Note:** Because `BarTransformer` converts `Bar` objects to `String` objects, the same rules for `String` now apply to `Bar`. That is, you can no longer use `Bar` as the response type of an API method, as primitives and enums are disallowed as API resource types. This also means that `Bar` can only be a request parameter type if used as a named parameter.**Note:** The source type for a transformer can be a raw generic type. This allows the transformer to handle transformation for all instances of the generic type.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
