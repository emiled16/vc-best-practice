---
name: mcp-docker
description: Use the Docker MCP gateway to inspect containers, images, volumes, Compose applications, and Docker-backed local environments. Use when the task involves local container debugging, Docker runtime inspection, or controlled Docker operations.
---

# Docker MCP

Use the Docker MCP gateway for Docker-aware operations.

## Workflow

1. Confirm whether the task is about local Docker state, Compose services, images, or containers.
2. Prefer read operations first: inspect running containers, logs, images, volumes, networks, and Compose state.
3. Use write actions only when the user explicitly wants Docker state changed.
4. Keep scope narrow to the relevant project, service, or container.

## Good Fits

- Inspect local containers or images.
- Debug Compose-backed development environments.
- Check container logs, health, and runtime metadata.
- Perform bounded Docker actions without dropping to raw shell commands.

## Guardrails

- Confirm Docker Desktop or the Docker MCP Toolkit is running before relying on the gateway.
- Prefer project- or service-specific actions over broad daemon-wide operations.
- Treat stop, delete, prune, and rebuild actions as higher risk than reads.
