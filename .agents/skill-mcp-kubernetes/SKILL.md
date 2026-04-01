---
name: mcp-kubernetes
description: Use the Kubernetes MCP server to inspect kubeconfig, namespaces, pods, events, generic resources, and Helm state across Kubernetes or OpenShift clusters. Use when the task involves cluster debugging, resource inspection, or controlled Kubernetes operations.
---

# Kubernetes MCP

Use the Kubernetes MCP server for cluster-aware operations.

## Workflow

1. Determine the target context and namespace before acting.
2. Start with read operations such as contexts, namespaces, pods, events, and resource gets.
3. Escalate to writes only when the user wants cluster state changed.
4. Keep scope narrow by using context and namespace arguments whenever possible.

## Good Fits

- Inspect current cluster configuration.
- Debug pods, events, deployments, or services.
- Check resource manifests and status.
- Inspect Helm releases when the `helm` toolset is enabled.

## Guardrails

- Prefer read-only investigation first.
- Be explicit about context and namespace to avoid touching the wrong cluster.
- Use least-privilege kube credentials and consider read-only server modes for routine debugging.
