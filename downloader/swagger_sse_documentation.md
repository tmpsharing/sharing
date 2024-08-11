
# Swagger and SSE Real-Time Endpoint Documentation

## User Query

**User:** Swagger doesn't show Java SSEemitter data in real-time.

**Assistant:** When using Swagger (OpenAPI) to document and test APIs that include Server-Sent Events (SSE) in Java, you may encounter limitations because Swagger UI does not natively support real-time updates or streaming data from an SSE endpoint. Swagger is primarily designed for documenting and testing RESTful APIs, which typically return responses upon request rather than continuous data streams.

Here's a general approach to address this:

1. **Documentation Purpose**:
   - Clearly document the SSE endpoint in your OpenAPI specification, indicating that it is an SSE endpoint and explaining how clients should consume the data.

2. **Testing SSE Endpoints**:
   - Use other tools like Postman or a simple JavaScript client to test SSE endpoints. Swagger UI won't be able to show real-time data, but these tools can handle streaming responses.

3. **Example Client**:
   - Provide an example client code in your API documentation to help users understand how to consume the SSE stream. For instance, a simple HTML + JavaScript example to consume SSE data.

### Example of OpenAPI Specification for SSE Endpoint

```yaml
openapi: 3.0.0
info:
  title: SSE Example API
  version: 1.0.0
paths:
  /sse-endpoint:
    get:
      summary: Server-Sent Events endpoint
      description: >
        This endpoint streams real-time data using Server-Sent Events (SSE). Clients should use an EventSource object to consume the data.
      responses:
        '200':
          description: A stream of real-time data
          content:
            text/event-stream:
              schema:
                type: string
                example: |
                  data: {"message": "This is a test message"}
```

### Example Client

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SSE Client</title>
</head>
<body>
  <h1>Server-Sent Events Example</h1>
  <div id="events"></div>

  <script>
    const eventSource = new EventSource('/sse-endpoint');
    eventSource.onmessage = function(event) {
      const newElement = document.createElement("div");
      newElement.textContent = event.data;
      document.getElementById("events").appendChild(newElement);
    };
  </script>
</body>
</html>
```

## Adding a Notification for Real-Time Endpoints

**User:** How to add a notification for an endpoint, indicating it is a real-time endpoint and should be opened in another browser tab?

**Assistant:** To add a notification in your Swagger documentation that indicates an endpoint is a real-time SSE endpoint and should be opened in another browser tab, you can enhance the description of the endpoint with a clear message. Here’s how you can do it:

### Enhancing OpenAPI Specification with a Notification

```yaml
openapi: 3.0.0
info:
  title: SSE Example API
  version: 1.0.0
paths:
  /sse-endpoint:
    get:
      summary: Server-Sent Events endpoint
      description: >
        **This endpoint streams real-time data using Server-Sent Events (SSE).**
        
        Please open this endpoint in another browser tab or use a tool that supports SSE such as Postman.

        Example: [SSE Client Example](#example-client)
      responses:
        '200':
          description: A stream of real-time data
          content:
            text/event-stream:
              schema:
                type: string
                example: |
                  data: {"message": "This is a test message"}
```

### Providing a Client Example in the Documentation

Additionally, provide a client example directly in your documentation. This can be added in the `description` field as a detailed markdown or in a separate section.

```yaml
openapi: 3.0.0
info:
  title: SSE Example API
  version: 1.0.0
paths:
  /sse-endpoint:
    get:
      summary: Server-Sent Events endpoint
      description: >
        **This endpoint streams real-time data using Server-Sent Events (SSE).**
        
        Please open this endpoint in another browser tab or use a tool that supports SSE such as Postman.

        ### Example Client
        
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>SSE Client</title>
        </head>
        <body>
          <h1>Server-Sent Events Example</h1>
          <div id="events"></div>

          <script>
            const eventSource = new EventSource('/sse-endpoint');
            eventSource.onmessage = function(event) {
              const newElement = document.createElement("div");
              newElement.textContent = event.data;
              document.getElementById("events").appendChild(newElement);
            };
          </script>
        </body>
        </html>
        ```
      responses:
        '200':
          description: A stream of real-time data
          content:
            text/event-stream:
              schema:
                type: string
                example: |
                  data: {"message": "This is a test message"}
```

### Steps to Implement

1. **Update the OpenAPI Specification**: Ensure the `description` field of your SSE endpoint is updated to include a clear notification about its real-time nature and the need to open it in another browser tab or use a tool like Postman.
   
2. **Include Example Client Code**: Provide an example client code directly in the OpenAPI description or in a separate section. This helps users understand how to consume the SSE endpoint.

3. **Publish and Share**: Ensure your updated OpenAPI documentation is published and accessible to the intended users.

By following these steps, your documentation will clearly communicate the nature of the SSE endpoint and provide users with the necessary instructions and examples to effectively use it.
