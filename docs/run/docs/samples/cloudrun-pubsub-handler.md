---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-pubsub-handler/
title: Handler for Pub/Sub messages \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:04.913443+00:00
---

# Handler for Pub/Sub messages  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-pubsub-handler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Handler for Pub/Sub messages Stay organized with collections  Save and categorize content based on your preferences. 

Service to handle messages delivered by a Cloud Pub/Sub Push subscription.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use Pub/Sub with Cloud Run tutorial](https://docs.cloud.google.com/run/docs/tutorials/pubsub)



## Code sample

### C#

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    app.MapPost("/", (Envelope envelope) =>
    {
        if (envelope?.Message?.Data == null)
        {
            app.Logger.LogWarning("Bad Request: Invalid Pub/Sub message format.");
            return Results.BadRequest();
        }
    
        var data = Convert.FromBase64String(envelope.Message.Data);
        var target = System.Text.Encoding.UTF8.GetString(data);
    
        app.Logger.LogInformation($"Hello {target}!");
    
        return Results.NoContent();
    });
    

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // WrappedMessage is the payload of a Pub/Sub event.
    //
    // For more information about receiving messages from a Pub/Sub event
    // see: https://cloud.google.com/pubsub/docs/push#receive_push
    type WrappedMessage struct {
    	Message struct {
    		Data []byte `json:"data,omitempty"`
    		ID   string `json:"id"`
    	} `json:"message"`
    	Subscription string `json:"subscription"`
    }
    
    // HelloPubSub receives and processes a Pub/Sub push message.
    func HelloPubSub(w http.ResponseWriter, r *http.Request) {
    	var m WrappedMessage
    	body, err := io.ReadAll(r.Body)
    	defer r.Body.Close()
    	if err != nil {
    		log.Printf("io.ReadAll: %v", err)
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    	// byte slice unmarshalling handles base64 decoding.
    	if err := json.Unmarshal(body, &m); err != nil {
    		log.Printf("json.Unmarshal: %v", err)
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    
    	name := string(m.Message.Data)
    	if name == "" {
    		name = "World"
    	}
    	log.Printf("Hello %s!", name)
    }
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.example.cloudrun.Body;
    import java.util.Base64;
    import org.apache.commons.lang3.StringUtils;
    import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.RequestBody;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestMethod;
    import org.springframework.web.bind.annotation.RestController;
    
    // PubsubController consumes a Pub/Sub message.
    @RestController
    public class PubSubController {
      @RequestMapping(value = "/", method = RequestMethod.POST)
      public ResponseEntity<String> receiveMessage(@RequestBody Body body) {
        // Get PubSub message from request body.
        Body.Message message = body.getMessage();
        if (message == null) {
          String msg = "Bad Request: invalid Pub/Sub message format";
          System.out.println(msg);
          return new ResponseEntity<>(msg, HttpStatus.BAD_REQUEST);
        }
    
        String data = message.getData();
        String target =
            !StringUtils.isEmpty(data) ? new String(Base64.getDecoder().decode(data)) : "World";
        String msg = "Hello " + target + "!";
    
        System.out.println(msg);
        return new ResponseEntity<>(msg, HttpStatus.OK);
      }
    }

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    app.post('/', (req, res) => {
      if (!req.body) {
        const msg = 'no Pub/Sub message received';
        console.error(`error: ${msg}`);
        res.status(400).send(`Bad Request: ${msg}`);
        return;
      }
      if (!req.body.message) {
        const msg = 'invalid Pub/Sub message format';
        console.error(`error: ${msg}`);
        res.status(400).send(`Bad Request: ${msg}`);
        return;
      }
    
      const pubSubMessage = req.body.message;
      const name = pubSubMessage.data
        ? Buffer.from(pubSubMessage.data, 'base64').toString().trim()
        : 'World';
    
      console.log(`Hello ${name}!`);
      res.status(204).send();
    });

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    @app.route("/", methods=["POST"])
    def index():
        """Receive and parse Pub/Sub messages."""
        envelope = request.get_json()
        if not envelope:
            msg = "no Pub/Sub message received"
            print(f"error: {msg}")
            return f"Bad Request: {msg}", 400
    
        if not isinstance(envelope, dict) or "message" not in envelope:
            msg = "invalid Pub/Sub message format"
            print(f"error: {msg}")
            return f"Bad Request: {msg}", 400
    
        pubsub_message = envelope["message"]
    
        name = "World"
        if isinstance(pubsub_message, dict) and "data" in pubsub_message:
            name = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
    
        print(f"Hello {name}!")
    
        return ("", 204)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
