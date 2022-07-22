# jiroxy
Jira Tasks Proxy Service for Jetbrains Tasks Tool (but not only)

# Usage

In order to use this service simply set your own env variables in `.env` file or pass to the docker command.

## Using .env file

There are several env vars you can use to control the service:

- `SERVER_PORT` - optional - set the port on which the service will be running (defaults to `8000`)
- `SYNC_EVERY_SECONDS` - optional - set number of seconds between the data sync from your Jira server (cache; defaults to `60`)
- `JIRA_API_KEY` - required - API key to access your Jira server
- `JIRA_QUERY_URL` - required - URL to your Jira API server with full path to query tasks (see example below)

### Example file

```bash
JIRA_API_KEY="SUPER_SECRET_KEY"

JIRA_QUERY_URL="https://JIRA.DOMAIN.COM/rest/api/2/search?jql=assignee%20%3D%20currentUser%28%29%20AND%20resolution%20%3D%20unresolved"

SERVER_PORT=8000

SYNC_EVERY_SECONDS=60
```

This example query URL will pull all your open tickets. You can improve this by adding your own encoded query.

## Building the image

This service is using the docker to run in isolated environment. You can also run it manually with python, but docker is the suggested way.

To build the image run:

```bash
docker build -t jiroxy:latest .
```

## Starting the service

To start the service using `.env` file run:

```bash
docker run -d -p 8000:8000 --env-file .env jiroxy:latest
```

Now you can see your tasks at `http://localhost:8000/`
