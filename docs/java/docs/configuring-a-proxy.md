---
url: https://docs.cloud.google.com/java/docs/configuring-a-proxy/
title: Configure a proxy \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:15.336079+00:00
---

# Configure a proxy  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/configuring-a-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Configure a proxy Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud client libraries use HTTPS and gRPC in underlying communication with the services. In both protocols, you can configure a proxy using `https.proxyHost` and, optionally, `https.proxyPort` properties.

## Configure a proxy with HTTP

For HTTP clients, you can configure a basic proxy by using `http.proxyHost` and related system properties, as documented by [Java Networking and Proxies](https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html).

For a custom proxy (for example, an authenticated proxy), provide a custom `HttpTransportFactory` to `GoogleCredentials`:
    
    
    import com.google.api.client.http.[HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html);
    import com.google.api.client.http.apache.v2.[ApacheHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.apache.v2.ApacheHttpTransport.html);
    import com.google.auth.http.[HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import org.apache.http.HttpHost;
    import org.apache.http.auth.AuthScope;
    import org.apache.http.auth.UsernamePasswordCredentials;
    import org.apache.http.client.CredentialsProvider;
    import org.apache.http.client.HttpClient;
    import org.apache.http.conn.routing.HttpRoutePlanner;
    import org.apache.http.impl.client.BasicCredentialsProvider;
    import org.apache.http.impl.client.ProxyAuthenticationStrategy;
    import org.apache.http.impl.conn.DefaultProxyRoutePlanner;
    
    
    import java.io.IOException;
    
    
    public class ProxyExample {
     public [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) getCredentials() throws IOException {
       [HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory.html) httpTransportFactory = getHttpTransportFactory(
           "some-host", 8080, "some-username", "some-password"
       );
    
    
       return [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)(httpTransportFactory);
     }
    
    
     public [HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory.html) getHttpTransportFactory(String proxyHost, int proxyPort, String proxyUsername, String proxyPassword) {
       HttpHost proxyHostDetails = new HttpHost(proxyHost, proxyPort);
       HttpRoutePlanner httpRoutePlanner = new DefaultProxyRoutePlanner(proxyHostDetails);
    
    
       CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
       credentialsProvider.setCredentials(
           new AuthScope(proxyHostDetails.getHostName(), proxyHostDetails.[getPort](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl.html#com_google_api_client_http_GenericUrl_getPort__)()),
           new UsernamePasswordCredentials(proxyUsername, proxyPassword)
       );
    
    
       HttpClient httpClient = [ApacheHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.apache.v2.ApacheHttpTransport.html).newDefaultHttpClientBuilder()
           .setRoutePlanner(httpRoutePlanner)
           .setProxyAuthenticationStrategy(ProxyAuthenticationStrategy.INSTANCE)
           .setDefaultCredentialsProvider(credentialsProvider)
           .build();
    
    
       final [HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html) httpTransport = new [ApacheHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.apache.v2.ApacheHttpTransport.html)(httpClient);
       return new [HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory.html)() {
         @Override
         public [HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html) create() {
           return httpTransport;
         }
       };
     }
    }
    

The preceding example requires `com.google.http-client:google-http-client-apache-v2`.

## Configure a proxy with a gRPC custom proxy configuration

For a custom proxy with gRPC, supply a `ProxyDetector` to the `ManagedChannelBuilder`:

Replace `PROXY_USERNAME`, `PROXY_PASSWORD`, `PROXY_HOST`, and `PROXY_PORT` with the credentials and address of your proxy.
    
    
    import com.google.api.core.[ApiFunction](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFunction.html);
    import com.google.api.gax.rpc.[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html);
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[CloudTasksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksSettings.html);
    import com.google.cloud.tasks.v2.stub.CloudTasksStubSettings;
    import io.grpc.HttpConnectProxiedSocketAddress;
    import io.grpc.ManagedChannelBuilder;
    import io.grpc.ProxiedSocketAddress;
    import io.grpc.ProxyDetector;
    
    import javax.annotation.Nullable;
    import java.io.IOException;
    import java.net.InetSocketAddress;
    import java.net.SocketAddress;
    
    public [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) getService() throws IOException {
      [TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html) transportChannelProvider =
          CloudTasksStubSettings.[defaultGrpcTransportProviderBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksSettings.html#com_google_cloud_tasks_v2_CloudTasksSettings_defaultGrpcTransportProviderBuilder__)()
              .setChannelConfigurator(
                  new ApiFunction<ManagedChannelBuilder, ManagedChannelBuilder>() {
                    @Override
                    public ManagedChannelBuilder apply(ManagedChannelBuilder managedChannelBuilder) {
                      return managedChannelBuilder.proxyDetector(
                          new ProxyDetector() {
                            @Nullable
                            @Override
                            public ProxiedSocketAddress proxyFor(SocketAddress socketAddress)
                                throws IOException {
                              return HttpConnectProxiedSocketAddress.newBuilder()
                                  .setUsername(PROXY_USERNAME)
                                  .setPassword(PROXY_PASSWORD)
                                  .setProxyAddress(new InetSocketAddress(PROXY_HOST, PROXY_PORT))
                                  .setTargetAddress((InetSocketAddress) socketAddress)
                                  .build();
                            }
                          });
                    }
                  })
              .build();
      [CloudTasksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksSettings.html) cloudTasksSettings =
          [CloudTasksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksSettings.html).newBuilder()
              .setTransportChannelProvider(transportChannelProvider)
              .build();
      return [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create(cloudTasksSettings);
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
