---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/overview/
title: google-api-client overview (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:22.117060+00:00
---

# google-api-client overview (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  google-api-client overview (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 

## 

## [com.google.api.client.googleapis](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis)

Google APIs.

## [com.google.api.client.googleapis.apache.v2](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.apache.v2)

Google APIs support based on the Apache HTTP Client.

## [com.google.api.client.googleapis.apache.v5](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.apache.v5)

Google APIs support based on the Apache HTTP Client v5.

## [com.google.api.client.googleapis.auth.oauth2](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2)

Google's additions to OAuth 2.0 authorization as specified in [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/OAuth2).

Before using this library, you must register your application at the [APIs Console](https://cloud.google.com/compute/docs/console). The result of this registration process is a set of values that are known to both Google and your application, such as the "Client ID", "Client Secret", and "Redirect URIs".

These are the typical steps of the web server flow based on an authorization code, as specified in [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/OAuth2WebServer):

  * Redirect the end user in the browser to the authorization page using [com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeRequestUrl) to grant your application access to the end user's protected data. 
  * Process the authorization response using com.google.api.client.auth.oauth2.AuthorizationCodeResponseUrl to parse the authorization code. 
  * Request an access token and possibly a refresh token using [com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeTokenRequest). 
  * Access protected resources using [com.google.api.client.googleapis.auth.oauth2.GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential). Expired access tokens will automatically be refreshed using the refresh token (if applicable). 



These are the typical steps of the browser-based client flow specified in [Using OAuth 2.0 for Client-side Applications](https://developers.google.com/identity/protocols/OAuth2UserAgent):

  * Redirect the end user in the browser to the authorization page using [com.google.api.client.googleapis.auth.oauth2.GoogleBrowserClientRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleBrowserClientRequestUrl) to grant your browser application access to the end user's protected data. 
  * Use the [Google API Client library for JavaScript](https://github.com/google/google-api-javascript-client) to process the access token found in the URL fragment at the redirect URI registered at the [APIs Console](https://cloud.google.com/compute/docs/consoles). 



## [com.google.api.client.googleapis.batch](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.batch)

Batch for Google API's.

## [com.google.api.client.googleapis.batch.json](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.batch.json)

JSON batch for Google API's.

## [com.google.api.client.googleapis.compute](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.compute)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Support for [Google Compute Engine](https://developers.google.com/compute/).

## [com.google.api.client.googleapis.extensions.android.accounts](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.extensions.android.accounts)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Utilities for Account Manager for Google accounts on Android Eclair (SDK 2.1) and later.

## [com.google.api.client.googleapis.extensions.android.gms.auth](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.extensions.android.gms.auth)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Utilities based on [Google Play services](https://developers.google.com/android/google-play-services/).

## [com.google.api.client.googleapis.extensions.appengine.auth.oauth2](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.extensions.appengine.auth.oauth2)

Google App Engine utilities for OAuth 2.0 for Google APIs.

## [com.google.api.client.googleapis.extensions.appengine.notifications](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.extensions.appengine.notifications)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Support for subscribing to topics and receiving notifications on servlet-based platforms.

## [com.google.api.client.googleapis.extensions.appengine.testing.auth.oauth2](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.extensions.appengine.testing.auth.oauth2)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.extensions.appengine.auth.oauth2` package.

## [com.google.api.client.googleapis.extensions.servlet.notifications](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.extensions.servlet.notifications)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Support for subscribing to topics and receiving notifications on servlet-based platforms.

## [com.google.api.client.googleapis.extensions.servlet.notifications.jakarta](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.extensions.servlet.notifications.jakarta)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Support for subscribing to topics and receiving notifications on servlet-based platforms using `jakarta.servlet` namespace.

## [com.google.api.client.googleapis.javanet](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.javanet)

Google API's support based on the `java.net` package.

## [com.google.api.client.googleapis.json](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.json)

Google's JSON support (see detailed package specification).

## Package Specification

User-defined Partial JSON data models allow you to defined Plain Old Java Objects (POJO's) to define how the library should parse/serialize JSON. Each field that should be included must have an @[com.google.api.client.util.Key](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Key.html) annotation. The field can be of any visibility (private, package private, protected, or public) and must not be static. By default, the field name is used as the JSON key. To override this behavior, simply specify the JSON key use the optional value parameter of the annotation, for example `@Key("name")`. Any unrecognized keys from the JSON are normally simply ignored and not stored. If the ability to store unknown keys is important, use com.google.api.client.json.GenericJson.

Let's take a look at a typical partial JSON-C video feed from the YouTube Data API (as specified in [YouTube Developer's Guide: JSON-C / JavaScript](https://developers.google.com/youtube/v3/code_samples/?csw=1))
    
    
     "data":{
      "updated":"2010-01-07T19:58:42.949Z",
                      "totalItems":800,
                      "startIndex":1,
                      "itemsPerPage":1,
                      "items":[
                              {"id":"hYB0mn5zh2c",
                                      "updated":"2010-01-07T13:26:50.000Z",
                                      "title":"Google Developers Day US - Maps API Introduction",
                                      "description":"Google Maps API Introduction ...",
                                      "tags":[
                                              "GDD07","GDD07US","Maps"],
                                  "player":{
                                  "default":"http://www.youtube.com/watch?v=hYB0mn5zh2c" },
                                  ...
                              }]}
     

Here's one possible way to design the Java data classes for this (each class in its own Java file):
    
    
     import com.google.api.client.util.*;
     import java.util.List;
    
     public class VideoFeed {
       @Key public int itemsPerPage;
       @Key public int startIndex;
       @Key public int totalItems;
       @Key public [DateTime](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.DateTime.html) updated;
       @Key public List<Video> items;
     }
    
     public class Video {
       @Key public String id;
       @Key public String title;
       @Key public [DateTime](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.DateTime.html) updated;
       @Key public String description;
       @Key public List<String> tags;
       @Key public Player player;
     }
    
     public class Player {
       // "default" is a Java keyword, so need to specify the JSON key manually
       @Key("default")
       public String defaultUrl;
     }
     

You can also use the @[com.google.api.client.util.Key](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Key.html) annotation to defined query parameters for a URL. For example:

{@code public class YouTubeUrl extends GoogleUrl {

@Key public String author;

@Key("max-results") public Integer maxResults;

public YouTubeUrl(String encodedUrl) { super(encodedUrl); this.alt = "jsonc"; } }

To work with the YouTube API, you first need to set up the  com.google.api.client.http.HttpTransport. For example:

{@code private static HttpTransport setUpTransport() throws IOException { HttpTransport result = new NetHttpTransport(); GoogleUtils.useMethodOverride(result); HttpHeaders headers = new HttpHeaders(); headers.setApplicationName("Google-YouTubeSample/1.0"); headers.gdataVersion = "2"; JsonCParser parser = new JsonCParser(); parser.jsonFactory = new GsonFactory(); transport.addParser(parser); // insert authentication code... return transport; } }

Now that we have a transport, we can execute a request to the YouTube API and parse the result:

{@code public static VideoFeed list(HttpTransport transport, YouTubeUrl url) throws IOException { HttpRequest request = transport.buildGetRequest(); request.url = url; return request.execute().parseAs(VideoFeed.class); } }

If the server responds with an error the  com.google.api.client.http.HttpRequest#execute method will throw an  com.google.api.client.http.HttpResponseException, which has an  com.google.api.client.http.HttpResponse field which can be parsed the same way as a success response inside of a catch block. For example:

{@code try { ... } catch (HttpResponseException e) { if (e.response.getParser() != null) { Error error = e.response.parseAs(Error.class); // process error response } else { String errorContentString = e.response.parseAsString(); // process error response as string } throw e; } }

NOTE: As you might guess, the library uses reflection to populate the user-defined data model. It's not quite as fast as writing the wire format parsing code yourself can potentially be, but it's a lot easier.

NOTE: If you prefer to use your favorite JSON parsing library instead (there are many of them listed for example on [json.org](http://json.org)), that's supported as well. Just call com.google.api.client.http.HttpRequest#execute() and parse the returned byte stream.

@since 1.0

@author Yaniv Inbar

## [com.google.api.client.googleapis.media](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media)

Media for Google API's.

## [com.google.api.client.googleapis.mtls](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.mtls)

Mutual TLS utilities for the Google API Client Library.

## [com.google.api.client.googleapis.notifications](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.notifications)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Support for notification channels to listen for changes to watched Google API resources.

## [com.google.api.client.googleapis.notifications.json](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.notifications.json)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
JSON-based notification handling for notification channels.

## [com.google.api.client.googleapis.notifications.json.gson](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.notifications.json.gson)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Notification channel handling based on the [GSON](https://github.com/google/gson/) JSON library.

## [com.google.api.client.googleapis.notifications.json.jackson2](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.notifications.json.jackson2)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Notification channel handling based on the [Jackson 2](http://wiki.fasterxml.com/JacksonRelease20) JSON library.

## [com.google.api.client.googleapis.services](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services)

Contains the basis for the generated service-specific libraries.

## [com.google.api.client.googleapis.services.json](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.json)

Contains the basis for the generated service-specific libraries based on the JSON format.

## [com.google.api.client.googleapis.services.protobuf](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.protobuf)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Contains the basis for the generated service-specific libraries based on the Protobuf format.

## [com.google.api.client.googleapis.testing](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis` package.

## [com.google.api.client.googleapis.testing.auth.oauth2](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.auth.oauth2)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.auth.oauth2` package.

## [com.google.api.client.googleapis.testing.compute](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.compute)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.compute` package.

## [com.google.api.client.googleapis.testing.json](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.json)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.json` package.

## [com.google.api.client.googleapis.testing.notifications](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.notifications)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.notifications` package.

## [com.google.api.client.googleapis.testing.services](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.services)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.services` package.

## [com.google.api.client.googleapis.testing.services.json](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.services.json)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.services.json` package.

## [com.google.api.client.googleapis.testing.services.protobuf](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.services.protobuf)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Test utilities for the `com.google.api.client.googleapis.protobuf` package.

## [com.google.api.client.googleapis.util](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.util)

Utilities for the Google API Client Library.

## [com.google.api.client.googleapis.xml.atom](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.xml.atom)

[com.google.api.client.util.Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
Utilities for Google's Atom XML implementation (see detailed package specification).

## Package Specification

User-defined Partial XML data models allow you to defined Plain Old Java Objects (POJO's) to define how the library should parse/serialize XML. Each field that should be included must have an @[com.google.api.client.util.Key](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Key.html) annotation. The field can be of any visibility (private, package private, protected, or public) and must not be static.

The optional value parameter of this @[com.google.api.client.util.Key](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Key.html) annotation specifies the XPath name to use to represent the field. For example, an XML attribute `a ` has an XPath name of `@a`, an XML element `<a>` has an XPath name of ` a `, and an XML text content has an XPath name of `text()`. These are named based on their usage with the [partial response/update syntax](https://developers.google.com/gdata/docs/2.0/reference?csw=1#PartialUpdate) for Google API's. If the @[com.google.api.client.util.Key](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Key.html) annotation is missing, the default is to use the Atom XML namespace and the Java field's name as the local XML name. By default, the field name is used as the JSON key. Any unrecognized XML is normally simply ignored and not stored. If the ability to store unknown keys is important, use [com.google.api.client.xml.GenericXml](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.xml.GenericXml.html).

Let's take a look at a typical partial Atom XML album feed from the Picasa Web Albums Data API:
    
    
     <?xml version='1.0' encoding='utf-8'?>
     <feed xmlns='http://www.w3.org/2005/Atom'
     xmlns:openSearch='http://a9.com/-/spec/opensearch/1.1/'
     xmlns:gphoto='http://schemas.google.com/photos/2007'>
     <link rel='http://schemas.google.com/g/2005#post'
     type='application/atom+xml'
     href='http://picasaweb.google.com/data/feed/api/user/liz' />
     <author>
     <name>Liz</name>
     </author>
     <openSearch:totalResults>1</openSearch:totalResults>
     <entry gd:etag='"RXY8fjVSLyp7ImA9WxVVGE8KQAE."'>
     <category scheme='http://schemas.google.com/g/2005#kind'
     term='http://schemas.google.com/photos/2007#album' />
     <title>lolcats</title>
     <summary>Hilarious Felines</summary>
     <gphoto:access>public</gphoto:access>
     </entry>
     </feed>
     

Here's one possible way to design the Java data classes for this (each class in its own Java file):
    
    
     import com.google.api.client.util.*;
     import java.util.List;
    
     public class Link {
    
       @Key("@href")
       public String href;
    
       @Key("@rel")
       public String rel;
    
       public static String find(List<Link> links, String rel) {
         if (links != null) {
           for (Link link : links) {
             if (rel.equals(link.rel)) {
               return link.href;
             }
           }
         }
         return null;
       }
     }
    
     public class Category {
    
       @Key("@scheme")
       public String scheme;
    
       @Key("@term")
       public String term;
    
       public static Category newKind(String kind) {
         Category category = new Category();
         category.scheme = "http://schemas.google.com/g/2005#kind";
         category.term = "http://schemas.google.com/photos/2007#" + kind;
         return category;
       }
     }
    
     public class AlbumEntry {
    
       @Key
       public String summary;
    
       @Key
       public String title;
    
       @Key("gphoto:access")
       public String access;
    
       public Category category = newKind("album");
    
       private String getEditLink() {
         return Link.find(links, "edit");
       }
     }
    
     public class Author {
    
       @Key
       public String name;
     }
    
     public class AlbumFeed {
    
       @Key
       public Author author;
    
       @Key("openSearch:totalResults")
       public int totalResults;
    
       @Key("entry")
       public List<AlbumEntry> photos;
    
       @Key("link")
       public List<Link> links;
    
       private String getPostLink() {
         return Link.find(links, "http://schemas.google.com/g/2005#post");
       }
     }
     

You can also use the @[com.google.api.client.util.Key](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Key.html) annotation to defined query parameters for a URL. For example:
    
    
     public class PicasaUrl extends GoogleUrl {
    
       @Key("max-results")
       public Integer maxResults;
    
       @Key
       public String kinds;
    
       public PicasaUrl(String url) {
         super(url);
       }
    
       public static PicasaUrl fromRelativePath(String relativePath) {
         PicasaUrl result = new PicasaUrl(PicasaWebAlbums.ROOT_URL);
         result.path += relativePath;
         return result;
       }
     }
     

To work with a Google API, you first need to set up the com.google.api.client.http.HttpTransport. For example:
    
    
     private static HttpTransport setUpTransport() throws IOException {
       HttpTransport result = new NetHttpTransport();
       GoogleUtils.useMethodOverride(result);
       HttpHeaders headers = new HttpHeaders();
       headers.setApplicationName("Google-PicasaSample/1.0");
       headers.gdataVersion = "2";
       AtomParser parser = new AtomParser();
       parser.namespaceDictionary = PicasaWebAlbumsAtom.NAMESPACE_DICTIONARY;
       transport.addParser(parser);
       // insert authentication code...
       return transport;
     }
     

Now that we have a transport, we can execute a partial GET request to the Picasa Web Albums API and parse the result:
    
    
     public static AlbumFeed executeGet(HttpTransport transport, PicasaUrl url) throws IOException {
       url.fields = GoogleAtom.getFieldsFor(AlbumFeed.class);
       url.kinds = "photo";
       url.maxResults = 5;
       HttpRequest request = transport.buildGetRequest();
       request.url = url;
       return request.execute().parseAs(AlbumFeed.class);
     }
     

If the server responds with an error the com.google.api.client.http.HttpRequest#execute method will throw an com.google.api.client.http.HttpResponseException, which has an com.google.api.client.http.HttpResponse field which can be parsed the same way as a success response inside of a catch block. For example:
    
    
     try {
       ...
     } catch (HttpResponseException e) {
       if (e.response.getParser() != null) {
         Error error = e.response.parseAs(Error.class);
         // process error response
       } else {
         String errorContentString = e.response.parseAsString();
         // process error response as string
       }
       throw e;
     }
     

To update an album, we use the transport to execute an efficient partial update request using the PATCH method to the Picasa Web Albums API:
    
    
     public AlbumEntry executePatchRelativeToOriginal
         (HttpTransport transport, AlbumEntry original) throws IOException {
       HttpRequest request = transport.buildPatchRequest();
       request.setUrl(getEditLink());
       request.headers.ifMatch = etag;
       AtomPatchRelativeToOriginalContent content = new AtomPatchRelativeToOriginalContent();
       content.namespaceDictionary = PicasaWebAlbumsAtom.NAMESPACE_DICTIONARY;
       content.originalEntry = original;
       content.patchedEntry = this;
       request.content = content;
       return request.execute().parseAs(AlbumEntry.class);
     }
    
     private static AlbumEntry updateTitle
         (HttpTransport transport, AlbumEntry album) throws IOException {
       AlbumEntry patched = album.clone();
       patched.title = "An alternate title";
       return patched.executePatchRelativeToOriginal(transport, album);
     }
     

To insert an album, we use the transport to execute a POST request to the Picasa Web Albums API:
    
    
     public AlbumEntry insertAlbum(HttpTransport transport, AlbumEntry entry) throws IOException {
       HttpRequest request = transport.buildPostRequest();
       request.setUrl(getPostLink());
       AtomContent content = new AtomContent();
       content.namespaceDictionary = PicasaWebAlbumsAtom.NAMESPACE_DICTIONARY;
       content.entry = entry;
       request.content = content;
       return request.execute().parseAs(AlbumEntry.class);
     }
     

To delete an album, we use the transport to execute a DELETE request to the Picasa Web Albums API:
    
    
     public void executeDelete(HttpTransport transport) throws IOException {
       HttpRequest request = transport.buildDeleteRequest();
       request.setUrl(getEditLink());
       request.headers.ifMatch = etag;
       request.execute().ignore();
     }
     

NOTE: As you might guess, the library uses reflection to populate the user-defined data model. It's not quite as fast as writing the wire format parsing code yourself can potentially be, but it's a lot easier.

NOTE: If you prefer to use your favorite XML parsing library instead (there are many of them), that's supported as well. Just call com.google.api.client.http.HttpRequest#execute() and parse the returned byte stream.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
