---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/api-access/
title: API access \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:50.534921+00:00
---

# API access  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/api-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  API access Stay organized with collections  Save and categorize content based on your preferences. 

You can use the API access deployment option when you are implementing a custom user interface and you want to send conversation messages using the API.

For each conversational turn at runtime, you use the [`runSession`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/runSession) method to send a user message and receive the agent application response.

## Create API access channel

To create an API access channel:

  1. Click **Deploy** at the top of the agent builder.
  2. Click **New channel**.
  3. Select **Set up API access**.
  4. Provide a channel name.
  5. Select or create an [agent application version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version).
  6. Use the optional **channel-specific behavior** setting if you want to override certain [agent application settings](https://docs.cloud.google.com/conversational-agents/ps/agent#agent-application-settings) for this specific channel.
  7. Click **Create channel**.



A dialog window is opened that shows the deployment ID and a sample `curl` command. On Linux and macOS systems, you can use this sample command to send a test message to your agent application.

## Authentication

The provided `curl` sample command uses `gcloud` to authenticate the request with your user credentials. For a production system, you should use service accounts for authentication. For more information, see [Authenticate to CX Agent Studio](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/authentication).

## Required IDs

To send a request, you need the following static IDs: `PROJECT_ID`, `REGION_ID`, `APPLICATION_ID`, and `DEPLOYMENT_ID`. You can find these IDs in the **Deployment ID** field provided in the dialog window's command sample for the channel. The values are defined in named path segments:
    
    
    projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID/deployments/DEPLOYMENT_ID
    

In addition, you need a dynamic `SESSION_ID`, which represents a unique conversation. This can be a generated string of your choosing, where the ID matches the regular expression `[a-zA-Z0-9][a-zA-Z0-9-_]{4,62}`.

## Call `runSession`

The following samples call the [`runSession`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/runSession) method, which is used to initiate a single turn interaction with the agent application in a session.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * REGION_ID: your region ID
  * APPLICATION_ID: your application ID
  * SESSION_ID: your session ID
  * DEPLOYMENT_ID: your application deployment ID



HTTP method and URL: 
    
    
    POST https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID/sessions/SESSION_ID:runSession

Request JSON body: 
    
    
    {
      "config": {
        "session": "projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID/sessions/SESSION_ID",
        "deployment": "projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID/deployments/DEPLOYMENT_ID",
      },
      "inputs": [
        {
          "text": "hi"
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID/sessions/SESSION_ID:runSession"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID/sessions/SESSION_ID:runSession" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "outputs": [
        {
          "text": "Hello there!",
          "turnCompleted": true,
          "turnIndex": 1,
          "diagnosticInfo": {...}
        }
      ]
    }
    

### Java

To authenticate to CX Agent Studio, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /*
     * Copyright 2025 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package com.google.cloud.ces.v1.samples;
    
    import com.google.cloud.ces.v1.RunSessionRequest;
    import com.google.cloud.ces.v1.RunSessionResponse;
    import com.google.cloud.ces.v1.SessionConfig;
    import com.google.cloud.ces.v1.SessionInput;
    import com.google.cloud.ces.v1.SessionServiceClient;
    import java.util.ArrayList;
    
    public class SyncRunSession {
    
      public static void main(String[] args) throws Exception {
        syncRunSession();
      }
    
      public static void syncRunSession() throws Exception {
        // This may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
          RunSessionRequest request =
              RunSessionRequest.newBuilder()
                  .setConfig(SessionConfig.newBuilder().build())
                  .addAllInputs(new ArrayList<SessionInput>())
                  .build();
          RunSessionResponse response = sessionServiceClient.runSession(request);
        }
      }
    }

### Python

To authenticate to CX Agent Studio, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import ces_v1
    from google.protobuf import field_mask_pb2
    
    def async_create_app():
        with ces_v1.AgentServiceClient() as agent_service_client:
            list_apps_request = ces_v1.ListAppsRequest(
                parent="projects/project-name/locations/us"
            )
            try:
                list_apps_page = agent_service_client.list_apps(request=list_apps_request)
                app_name = next(iter(list_apps_page)).name
            except StopIteration:
                print("No apps found.")
                return
    
            print(f"Using appName {app_name} to grab App")
    
            get_app_request = ces_v1.GetAppRequest(name=app_name)
            app = agent_service_client.get_app(request=get_app_request)
            print(f"Using app to either createAgent / updateApp {app}")
    
            # If there is no agent, please uncomment this part
            # # Create Agent
            # create_agent_request = ces_v1.CreateAgentRequest(
            #     parent=app_name,
            #     agent=ces_v1.Agent(display_name="agent-1"),
            # )
            # agent_response = agent_service_client.create_agent(request=create_agent_request)
    
            # List Agents
            list_agents_request = ces_v1.ListAgentsRequest(parent=app_name)
            try:
                list_agents_page = agent_service_client.list_agents(request=list_agents_request)
                agent = next(iter(list_agents_page))
                agent_name = agent.name
            except StopIteration:
                print(f"No agents found for app {app_name}.")
                return
    
            print(f"Using agent {agent_name} to update Agent")
    
            # Update App to have root agent
            app.root_agent = agent_name
            update_app_request = ces_v1.UpdateAppRequest(
                app=app,
                update_mask=field_mask_pb2.FieldMask(paths=["root_agent"]),
            )
            update_app_response = agent_service_client.update_app(request=update_app_request)
            print(f"Update App response: {update_app_response}")
    
            # runSession
            with ces_v1.SessionServiceClient() as session_service_client:
                session_name = f"{app_name}/sessions/session-1"
                config = ces_v1.SessionConfig(session=session_name)
                input_ = ces_v1.SessionInput(text="Hello World!")
                inputs = [input_]
                session_request = ces_v1.RunSessionRequest(config=config, inputs=inputs)
                session_response = session_service_client.run_session(request=session_request)
                print(f"Run session response: {session_response}")
    
    if __name__ == "__main__":
        async_create_app()

### Node.js

To authenticate to CX Agent Studio, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import {AgentServiceClient, SessionServiceClient} from '../src/v1';
    
    async function main() {
      const agentServiceClient = new AgentServiceClient();
      const sessionServiceClient = new SessionServiceClient();
      try {
        const listAppsRequest = {
          parent: 'projects/project-name/locations/us',
        };
    
        const listAppsIterator = agentServiceClient.listAppsAsync(listAppsRequest);
        let firstApp;
        for await (const app of listAppsIterator) {
          firstApp = app;
          break;
        }
    
        if (!firstApp) {
          console.log('No apps found.');
          return;
        }
        const appName = firstApp.name!;
    
        console.log(`Using appName ${appName} to grab App`);
    
        const [app] = await agentServiceClient.getApp({name: appName});
        console.log('Using app to either createAgent / updateApp', app);
    
        // If there is no agent, please uncomment this part
        // // Create Agent
        // const createAgentRequest = {
        //   parent: appName,
        //   agent: {displayName: 'agent-1'},
        // };
        // const [agentResponse] =
        //   await agentServiceClient.createAgent(createAgentRequest);
    
        // List Agents
        const listAgentsRequest = {parent: appName};
        const listAgentsIterator =
            agentServiceClient.listAgentsAsync(listAgentsRequest);
        let agent;
        for await (const a of listAgentsIterator) {
          agent = a;
          break;
        }
    
        if (!agent) {
          console.log(`No agents found for app ${appName}.`);
          return;
        }
        const agentName = agent.name!;
    
        console.log(`Using agent ${agentName} to update Agent`);
    
        // Update App to have root agent
        app.rootAgent = agentName;
        const updateAppRequest = {
          app: app,
          updateMask: {
            paths: ['root_agent'],
          },
        };
        const [updateAppResponse] =
            await agentServiceClient.updateApp(updateAppRequest);
        console.log('Update App response:', updateAppResponse);
    
        // runSession
        const sessionName = `${appName}/sessions/session-1`;
        const config = {session: sessionName};
        const input = {text: 'Hello World!'};
        const inputs = [input];
        const sessionRequest = {config: config, inputs: inputs};
        const [sessionResponse] =
            await sessionServiceClient.runSession(sessionRequest);
        console.log('Run session response:', sessionResponse);
      } catch (err) {
        console.error('An error occurred:', err);
      } finally {
        await agentServiceClient.close();
        await sessionServiceClient.close();
      }
    }
    
    main();

## Call `BidiRunSession`

As an alternative to `runSession`, you can use [`BidiRunSession`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService.BidiRunSession) to establish a bidirectional streaming connection with the agent application.

### Go

To authenticate to CX Agent Studio, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // A simple websocket client to interact with BidiRunSession with audio input
    // and output.
    //
    // Initialize your new module:
    //   - mkdir mypackage
    //   - cd mypackage
    //   - go mod init mypackage
    //
    // Install non-standard dependencies:
    //   - Install PortAudio C library using instructions at
    //     https://files.portaudio.com/docs/v19-doxydocs/tutorial_start.html
    //   - go get azul3d.org/engine
    //   - go get github.com/gordonklaus/portaudio
    //   - go get github.com/gorilla/websocket
    //
    // Usage
    //
    //	go run main.go -access_token=$(gcloud auth print-access-token) \
    //	  -location=YOUR_LOCATION \
    //	  -app=YOUR_APP_NAME \
    //	  -deployment=YOUR_DEPLOYMENT_NAME
    package main
    
    import (
    	"bytes"
    	"crypto/rand"
    	"encoding/base64"
    	"encoding/binary"
    	"encoding/hex"
    	"encoding/json"
    	"flag"
    	"fmt"
    	"log"
    	"net/http"
    	"net/url"
    	"os"
    	"os/signal"
    	"strings"
    	"sync"
    
    	"azul3d.org/engine/audio"
    	"github.com/gordonklaus/portaudio"
    	"github.com/gorilla/websocket"
    )
    
    var addr = flag.String("addr", "ces.googleapis.com", "API service address.")
    var location = flag.String("location", "us", "API service location.")
    var accessToken = flag.String("access_token", "", "Access token.")
    var app = flag.String("app",
    	"",
    	"App name in the form "+
    		"projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID.")
    var deployment = flag.String("deployment",
    	"",
    	"Deployment name in the form "+
    		"projects/PROJECT_ID/locations/REGION_ID/apps/APPLICATION_ID/deployments/DEPLOYMENT_ID.")
    var audioSampleRate = flag.Int("audio_sample_rate",
    	16000,
    	"Desired audio sample rate in Hz (e.g., 8000, 16000, 24000).")
    
    var (
    	audioBuffer bytes.Buffer
    	bufferMutex sync.Mutex
    	wg          sync.WaitGroup
    )
    
    type BidiSessionServerMessage struct {
    	SessionOutput      *SessionOutput      `json:"sessionOutput"`
    	RecognitionResult  *RecognitionResult  `json:"recognitionResult"`
    	InterruptionSignal *InterruptionSignal `json:"interruptionSignal"`
    	EndSession         *EndSession         `json:"endSession"`
    }
    
    type SessionOutput struct {
    	Audio string `json:"audio"`
    	Text  string `json:"text"`
    }
    
    type RecognitionResult struct {
    	Transcript string `json:"transcript"`
    }
    
    type InterruptionSignal struct {
    }
    
    type EndSession struct {
    	Metadata struct{} `json:"metadata"`
    }
    
    const defaultSampleRateHertz = 16000
    
    // 100ms
    const defaultChunkLength = 100
    
    // 16000 (sample rate hertz) * 100/1000 (100ms) * 2 (16 bit)
    const defaultChunkSize = defaultSampleRateHertz * defaultChunkLength / 1000 * 2
    
    func main() {
    	flag.Parse()
    	log.SetFlags((log.LstdFlags | log.Lshortfile | log.Lmicroseconds) &^ log.Ldate)
    
    	u := url.URL{Scheme: "wss",
    		Host: *addr,
    		Path: "/ws/google.cloud.ces.v1.SessionService/BidiRunSession/locations/" +
    			*location}
    	if strings.Contains(*addr, "localhost") {
    		u = url.URL{Scheme: "ws", Host: *addr, Path: "/ws"}
    	}
    
    	h := make(http.Header)
    	h.Add("Content-Type", "application/json")
    	h.Add("Authorization", "Bearer "+*accessToken)
    
    	conn, _, err := websocket.DefaultDialer.Dial(u.String(), h)
    	if err != nil {
    		log.Fatal("dial:", err)
    	}
    
    	interrupt := make(chan os.Signal, 1)
    	signal.Notify(interrupt, os.Interrupt)
    
    	portaudio.Initialize()
    	defer portaudio.Terminate()
    
    	inDev, err := portaudio.DefaultInputDevice()
    	if err != nil {
    		log.Fatal(err)
    	}
    	log.Printf("Input device: %v", inDev.Name)
    	outDev, err := portaudio.DefaultOutputDevice()
    	if err != nil {
    		log.Fatal(err)
    	}
    	log.Printf("Output device: %v", outDev.Name)
    
    	randomBytes := make([]byte, 8)
    	if _, err := rand.Read(randomBytes); err != nil {
    		log.Fatal(err)
    	}
    	session := fmt.Sprintf("%v/sessions/%v",
    		*app,
    		hex.EncodeToString(randomBytes))
    	log.Printf("Session: %v", session)
    
    	configMessage := map[string]any{
    		"config": map[string]any{
    			"session": session,
    			"inputAudioConfig": map[string]any{
    				"audioEncoding":   "LINEAR16",
    				"sampleRateHertz": *audioSampleRate,
    			},
    			"outputAudioConfig": map[string]any{
    				"audioEncoding":   "LINEAR16",
    				"sampleRateHertz": *audioSampleRate,
    			},
    			"deployment": *deployment,
    			// "debugMode": true,
    		},
    	}
    	jsonConfigMsg, err := json.Marshal(configMessage)
    	if err != nil {
    		log.Fatal(err)
    	}
    	if err = conn.WriteMessage(websocket.TextMessage,
    		[]byte(jsonConfigMsg)); err != nil {
    		log.Fatal(err)
    	}
    	log.Printf("Sent config: %s", string(jsonConfigMsg))
    
    	framesPerBuffer := defaultChunkSize / 2
    	stream, err := portaudio.OpenDefaultStream(1,
    		1,
    		float64(*audioSampleRate),
    		framesPerBuffer,
    		func(in, out []float32) {
    			// Lock the buffer to avoid data race
    			bufferMutex.Lock()
    			defer bufferMutex.Unlock()
    
    			// Output processing (Server to Speaker)
    			bytesPerSample := 2
    			bytesToRead := framesPerBuffer * bytesPerSample
    			audioChunk := make([]byte, bytesToRead)
    			nBytes, _ := audioBuffer.Read(audioChunk)
    			if nBytes > 0 && audioBuffer.Len() == 0 {
    				wg.Done()
    			}
    			audioChunk = audioChunk[:nBytes]
    
    			// LINEAR16 audio encoding
    			var speakerPcm16 []int16
    			numPcm16Samples := nBytes / 2
    			speakerPcm16 = make([]int16, numPcm16Samples)
    			for i := 0; i < numPcm16Samples; i++ {
    				if (i*2 + 2) <= len(audioChunk) {
    					speakerPcm16[i] = int16(
    						binary.LittleEndian.Uint16(audioChunk[i*2 : (i+1)*2]))
    				}
    			}
    
    			for i := 0; i < framesPerBuffer; i++ {
    				if i < len(speakerPcm16) {
    					out[i] = float32(audio.Int16ToFloat64(speakerPcm16[i]))
    				} else {
    					out[i] = 0
    				}
    			}
    
    			// Input processing (Mic to Server)
    			micPcm16 := make([]int16, len(in))
    			for i, f := range in {
    				micPcm16[i] = audio.Float64ToInt16(float64(f))
    			}
    
    			// LINEAR16 mic audio
    			var inputBuf []byte
    			buf := new(bytes.Buffer)
    			binary.Write(buf, binary.LittleEndian, micPcm16)
    			inputBuf = buf.Bytes()
    
    			audioMessage := map[string]any{
    				"realtimeInput": map[string]any{
    					"audio": base64.StdEncoding.EncodeToString(inputBuf),
    				},
    			}
    			jsonAudioMsg, err := json.Marshal(audioMessage)
    			if err != nil {
    				log.Fatal(err)
    			}
    			if err = conn.WriteMessage(websocket.TextMessage,
    				[]byte(jsonAudioMsg)); err != nil {
    				// log.Print(err)
    			}
    		})
    	if err != nil {
    		log.Fatalf("Error opening stream: %v", err)
    	}
    	defer stream.Close()
    	if err := stream.Start(); err != nil {
    		log.Fatalf("Error starting stream: %v", err)
    	}
    
    	serverHalfClose := make(chan struct{})
    	go func() {
    		// Signal completion when server half-close is received.
    		defer close(serverHalfClose)
    		for {
    			_, message, err := conn.ReadMessage()
    			if err != nil {
    				log.Printf("websocket read error:%v", err)
    				break
    			}
    			bidiSessionServerMessage := BidiSessionServerMessage{}
    			json.Unmarshal(message, &bidiSessionServerMessage)
    			if bidiSessionServerMessage.SessionOutput != nil &&
    				bidiSessionServerMessage.SessionOutput.Audio != "" {
    			} else {
    				log.Println(string(message))
    			}
    			if bidiSessionServerMessage.InterruptionSignal != nil {
    				bufferMutex.Lock()
    				if audioBuffer.Len() != 0 {
    					audioBuffer.Reset()
    					wg.Done()
    				}
    				bufferMutex.Unlock()
    			}
    			if bidiSessionServerMessage.EndSession != nil {
    				log.Printf("Received EndSession signal, closing the stream...")
    				interrupt <- os.Interrupt
    				break
    			}
    			if bidiSessionServerMessage.SessionOutput != nil &&
    				bidiSessionServerMessage.SessionOutput.Audio != "" {
    				audioBytes, err := base64.StdEncoding.DecodeString(
    					bidiSessionServerMessage.SessionOutput.Audio)
    				if err != nil {
    					log.Fatal(err)
    				}
    				bufferMutex.Lock()
    				if audioBuffer.Len() == 0 {
    					wg.Add(1)
    				}
    				audioBuffer.Write(audioBytes)
    				bufferMutex.Unlock()
    			}
    		}
    	}()
    
    	<-interrupt
    
    	if strings.Contains(*addr, "localhost") {
    		log.Println(
    			"Received interrupt. Initiating graceful shutdown (half-close)...")
    		if err = conn.WriteMessage(
    			websocket.TextMessage, []byte("half-close")); err != nil {
    			log.Printf("Error sending half-close: %v", err)
    		}
    	} else {
    		log.Fatal("Terminating...")
    	}
    
    	<-serverHalfClose
    	wg.Wait()
    
    	log.Println("Graceful termination complete. Closing connection.")
    }

### Java

To authenticate to CX Agent Studio, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /*
     * Copyright 2025 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package com.example.app;
    
    import com.google.auth.oauth2.GoogleCredentials;
    import com.google.cloud.ces.v1.BidiSessionClientMessage;
    import com.google.cloud.ces.v1.BidiSessionServerMessage;
    import com.google.cloud.ces.v1.SessionConfig;
    import com.google.cloud.ces.v1.SessionInput;
    import com.google.protobuf.util.JsonFormat;
    import java.net.URI;
    import java.nio.ByteBuffer;
    import java.nio.charset.StandardCharsets;
    import java.util.Collections;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.UUID;
    import java.util.concurrent.CountDownLatch;
    import java.util.concurrent.TimeUnit;
    import org.java_websocket.client.WebSocketClient;
    import org.java_websocket.handshake.ServerHandshake;
    
    public class Hello {
    
      public static void main(String[] args) throws Exception {
        asyncBidiRunSession();
      }
    
      public static void asyncBidiRunSession() throws Exception {
        // This may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        String sessionId = "session-name";
        if (sessionId.isEmpty()) {
          sessionId = UUID.randomUUID().toString();
        }
        String appResourceName = "projects/project-name/locations/us/apps/app-name";
        String sessionName = appResourceName + "/sessions/" + sessionId;
        String query = "Do you have t-shirt with a cat on it?";
        String query2 = "What is the weather today?";
    
        URI uri =
            new URI(
                "wss://ces.googleapis.com/ws/google.cloud.ces.v1.SessionService/BidiRunSession/locations/us");
    
        GoogleCredentials credentials =
            GoogleCredentials.getApplicationDefault()
                .createScoped(
                    Collections.singletonList("https://www.googleapis.com/auth/cloud-platform"));
        credentials.refreshIfExpired();
        String token = credentials.getAccessToken().getTokenValue();
        Map<String, String> headers = new HashMap<>();
        headers.put("Authorization", "Bearer " + token);
    
        CountDownLatch latch = new CountDownLatch(1);
    
        WebSocketClient client =
            new WebSocketClient(uri, headers) {
              @Override
              public void onOpen(ServerHandshake handshakedata) {
                System.out.println("WebSocket connection opened");
                try {
                  // 1. Send config message
                  BidiSessionClientMessage configMessage =
                      BidiSessionClientMessage.newBuilder()
                          .setConfig(SessionConfig.newBuilder().setSession(sessionName))
                          .build();
                  String configJson =
                      JsonFormat.printer()
                          .preservingProtoFieldNames()
                          .omittingInsignificantWhitespace()
                          .print(configMessage);
                  System.out.println("Sending config: " + configJson);
                  send(configJson);
    
                  // 2. Send query message
                  BidiSessionClientMessage queryMessage =
                      BidiSessionClientMessage.newBuilder()
                          .setRealtimeInput(SessionInput.newBuilder().setText(query))
                          .build();
                  String queryJson =
                      JsonFormat.printer()
                          .preservingProtoFieldNames()
                          .omittingInsignificantWhitespace()
                          .print(queryMessage);
                  System.out.println("Sending query: " + queryJson);
                  send(queryJson);
    
                  // 3. Send query message 2
                  BidiSessionClientMessage queryMessage2 =
                      BidiSessionClientMessage.newBuilder()
                          .setRealtimeInput(SessionInput.newBuilder().setText(query2))
                          .build();
                  String queryJson2 =
                      JsonFormat.printer()
                          .preservingProtoFieldNames()
                          .omittingInsignificantWhitespace()
                          .print(queryMessage2);
                  System.out.println("Sending query 2: " + queryJson2);
                  send(queryJson2);
                } catch (Exception e) {
                  e.printStackTrace();
                  latch.countDown();
                }
              }
    
              @Override
              public void onMessage(String message) {
                System.out.println("===============");
                System.out.println("Received message: " + message);
                try {
                  BidiSessionServerMessage.Builder builder = BidiSessionServerMessage.newBuilder();
                  JsonFormat.parser().ignoringUnknownFields().merge(message, builder);
                  BidiSessionServerMessage response = builder.build();
                  System.out.println("Parsed response: " + response);
                } catch (Exception e) {
                  System.err.println("Failed to parse message: " + e.getMessage());
                }
              }
    
              @Override
              public void onMessage(ByteBuffer bytes) {
                System.out.println("===============");
                String message = StandardCharsets.UTF_8.decode(bytes).toString();
                System.out.println("Received message: " + message);
              }
    
              @Override
              public void onClose(int code, String reason, boolean remote) {
                System.out.println(
                    "WebSocket connection closed by "
                        + (remote ? "remote peer" : "us")
                        + " with code "
                        + code
                        + " and reason: "
                        + reason);
                latch.countDown();
              }
    
              @Override
              public void onError(Exception ex) {
                System.err.println("WebSocket error: " + ex.getMessage());
                ex.printStackTrace();
                latch.countDown();
              }
            };
    
        try {
          System.out.println("Connecting to WebSocket: " + uri);
          client.connect();
          latch.await(10, TimeUnit.SECONDS);
        } finally {
          client.close();
        }
      }
    }

### Python

To authenticate to CX Agent Studio, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import threading
    import time
    import uuid
    
    import google.auth
    import google.auth.transport.requests
    import websocket
    from google.protobuf import json_format
    
    
    from google.cloud import ces_v1
    
    def async_bidi_run_session():
        """Demonstrates how to use the BidiRunSession WebSocket endpoint."""
        session_id = "session_name"
        if not session_id:
            session_id = str(uuid.uuid4())
    
        app_resource_name = "projects/project_name/locations/us/apps/app_name"
        session_name = f"{app_resource_name}/sessions/{session_id}"
        query = "Do you have t-shirt with a cat on it?"
        query2 = "What is the weather today?"
    
        uri = "wss://ces.googleapis.com/ws/google.cloud.ces.v1.SessionService/BidiRunSession/locations/us"
    
        try:
            credentials, _ = google.auth.default(
                scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
            request = google.auth.transport.requests.Request()
            credentials.refresh(request)
            token = credentials.token
            headers = {"Authorization": f"Bearer {token}"}
        except Exception as e:
            print(f"Failed to get credentials: {e}")
            return
    
        def on_open(ws):
            print("WebSocket connection opened")
            try:
                # 1. Send config message
                config_message = ces_v1.BidiSessionClientMessage(
                    config=ces_v1.SessionConfig(session=session_name)
                )
                config_json = json_format.MessageToJson(
                    config_message._pb, preserving_proto_field_name=False, indent=0
                ).replace("\\n", "")
                print(f"Sending config: {config_json}")
                ws.send(config_json)
    
                # 2. Send query message
                query_message = ces_v1.BidiSessionClientMessage(
                    realtime_input=ces_v1.SessionInput(text=query)
                )
                query_json = json_format.MessageToJson(
                    query_message._pb, preserving_proto_field_name=False, indent=0
                ).replace("\\n", "")
                print(f"Sending query: {query_json}")
                ws.send(query_json)
    
                # 3. Send query message 2
                query_message2 = ces_v1.BidiSessionClientMessage(
                    realtime_input=ces_v1.SessionInput(text=query2)
                )
                query_json2 = json_format.MessageToJson(
                    query_message2._pb, preserving_proto_field_name=False, indent=0
                ).replace("\\n", "")
                print(f"Sending query 2: {query_json2}")
                ws.send(query_json2)
            except Exception as e:
                print(f"Error during on_open: {e}")
                ws.close()
    
        def on_message(ws, message):
            print("===============")
            print(f"Received message: {message}")
            try:
                response_pb = ces_v1.BidiSessionServerMessage()._pb
                json_format.Parse(
                    message,
                    response_pb,
                    ignore_unknown_fields=True,
                )
                response = ces_v1.BidiSessionServerMessage(response_pb)
                print(f"Parsed response: {response}")
            except Exception as e:
                print(f"Failed to parse message: {e}")
    
        def on_error(ws, error):
            print(f"WebSocket error: {error}")
    
        def on_close(ws, close_status_code, close_msg):
            print(
                "WebSocket connection closed"
                f" with code {close_status_code}"
                f" and reason: {close_msg}"
            )
    
        print(f"Connecting to WebSocket: {uri}")
        ws_app = websocket.WebSocketApp(
            uri,
            header=headers,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )
    
        wst = threading.Thread(target=ws_app.run_forever)
        wst.daemon = True
        wst.start()
    
        print("Waiting for 10 seconds for messages...")
        time.sleep(10)
        print("10 seconds elapsed, closing connection.")
        ws_app.close()
        wst.join()
    
    
    if __name__ == "__main__":
        async_bidi_run_session()

### Node.js

To authenticate to CX Agent Studio, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import {GoogleAuth} from 'google-gax';
    import {WebSocket} from 'ws';
    
    async function main() {
      const sessionId = 'session-name';
      const appResourceName =
          'projects/project-name/locations/us/apps/app-name';
      const sessionName = `${appResourceName}/sessions/${sessionId}`;
      const query = 'Do you have t-shirt with a cat on it?';
      const query2 = 'What is the weather today?';
    
      console.log(`Starting bidi session with session name: ${sessionName}`);
    
      const uri =
          'wss://ces.googleapis.com/ws/google.cloud.ces.v1.SessionService/BidiRunSession/locations/us';
    
      let token;
      try {
        const auth = new GoogleAuth({
          scopes: ['https://www.googleapis.com/auth/cloud-platform'],
        });
        token = await auth.getAccessToken();
      } catch (e) {
        console.error(`Failed to get credentials: ${e}`);
        return;
      }
    
      const headers = {Authorization: `Bearer ${token}`};
      const ws = new WebSocket(uri, {headers});
    
      ws.on('open', () => {
        console.log('WebSocket connection opened');
        try {
          // 1. Send config message
          const configMessage = {
            config: {session: sessionName},
          };
          const configJson = JSON.stringify(configMessage);
          console.log(`Sending config: ${configJson}`);
          ws.send(configJson);
    
          // 2. Send query message
          const queryMessage = {
            realtimeInput: {text: query},
          };
          const queryJson = JSON.stringify(queryMessage);
          console.log(`Sending query: ${queryJson}`);
          ws.send(queryJson);
    
          // 3. Send query message 2
          const queryMessage2 = {
            realtimeInput: {text: query2},
          };
          const queryJson2 = JSON.stringify(queryMessage2);
          console.log(`Sending query 2: ${queryJson2}`);
          ws.send(queryJson2);
        } catch (e) {
          console.error(`Error during on_open: ${e}`);
          ws.close();
        }
      });
    
      ws.on('message', message => {
        console.log('===============');
        console.log(`Received message: ${message}`);
      });
    
      ws.on('error', err => {
        console.error(`WebSocket error: ${err}`);
      });
    
      ws.on('close', (code, reason) => {
        console.log(
            `WebSocket connection closed with code ${code} and reason: ${reason}`);
      });
    
      console.log('Waiting for 10 seconds for messages...');
      await new Promise(resolve => setTimeout(resolve, 10000));
      console.log('10 seconds elapsed, closing connection.');
      ws.close();
    }
    
    main();

In addition, if you are using `ces.googleapis.com` as the `apiEndpoint` with a gRPC client library, you must also set `x-goog-request-params` in `otherArgs` to a specific location. For example, using the [Node.js client library](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/library#nodejs):
    
    
    const sessionClient = new SessionServiceClient({
     apiEndpoint: 'ces.googleapis.com'
    });
    
    
    const grpc = require('@grpc/grpc-js');
    const callOptions = {
      otherArgs: {headers: {'x-goog-request-params': `location=locations/us`}}
    };
    
    stream = sessionClient.bidiRunSession(callOptions);
    

if you are using `ces.us.rep.googleapis.com` or `ces.eu.rep.googleapis.com`, you don't need to set `x-goog-request-params`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
