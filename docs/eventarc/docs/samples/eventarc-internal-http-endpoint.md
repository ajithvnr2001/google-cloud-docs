---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-internal-http-endpoint/
title: Receive Pub/Sub events at an internal HTTP endpoint in a VPC network \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:45.540371+00:00
---

# Receive Pub/Sub events at an internal HTTP endpoint in a VPC network  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-internal-http-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Receive Pub/Sub events at an internal HTTP endpoint in a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

Creates an internal HTTP endpoint in a Virtual Private Cloud (VPC) network that receives Pub/Sub message events using Eventarc. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Receive Pub/Sub events at an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-vpc-internal-endpoint)



## Code sample

### Python

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #!/usr/bin/env python3
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import logging
    
    class S(BaseHTTPRequestHandler):
        def _set_response(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
    
        def do_GET(self):
            logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
            self._set_response()
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
    
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                    str(self.path), str(self.headers), post_data.decode('utf-8'))
    
            self._set_response()
            self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
    
    def run(server_class=HTTPServer, handler_class=S, port=80):
        logging.basicConfig(level=logging.INFO)
        server_address = ('', port)
        http_server = server_class(server_address, handler_class)
        logging.info('Starting HTTP Server at port %d...\n', port)
        try:
            http_server.serve_forever()
        except KeyboardInterrupt:
            pass
        http_server.server_close()
        logging.info('Stopping HTTP Server...\n')
    
    if __name__ == '__main__':
        from sys import argv
    
        if len(argv) == 2:
            run(port=int(argv[1]))
        else:
            run()

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
