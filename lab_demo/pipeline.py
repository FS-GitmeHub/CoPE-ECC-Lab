"""Dependency-free, deterministic task ordering for an isolated test lab."""

from collections.abc import Mapping, Sequence
from heapq import heappop, heappush


def plan_tasks(tasks: Mapping[str, Sequence[str]]) -> list[str]:
    """Return a deterministic topological order, rejecting invalid graphs."""
    if not isinstance(tasks, Mapping):
        raise TypeError("tasks must be a mapping")
    indegree: dict[str, int] = {}
    dependents: dict[str, set[str]] = {}
    for name in tasks:
        if not isinstance(name, str) or not name:
            raise ValueError("task names must be non-empty strings")
        indegree[name] = 0
        dependents[name] = set()
    for name, requirements in tasks.items():
        if isinstance(requirements, (str, bytes)) or not isinstance(requirements, Sequence):
            raise TypeError("dependencies must be sequences of task names")
        seen: set[str] = set()
        for dep in requirements:
            if dep not in indegree:
                raise ValueError(f"unknown dependency {dep!r}")
            if dep in seen:
                raise ValueError(f"duplicate dependency {dep!r}")
            seen.add(dep)
            dependents[dep].add(name)
            indegree[name] += 1
    ready: list[str] = []
    for name, count in indegree.items():
        if count == 0:
            heappush(ready, name)
    result: list[str] = []
    while ready:
        name = heappop(ready)
        result.append(name)
        for later in dependents[name]:
            indegree[later] -= 1
            if indegree[later] == 0:
                heappush(ready, later)
    if len(result) != len(tasks):
        raise ValueError("dependency cycle detected")
    return result
