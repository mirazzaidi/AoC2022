from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Directory = None
    children: List[Directory] = field(default_factory=list)

    def add_child(self, child):
        self.children.append(child)

    def total_size(self):
        size = 0
        for child in self.children:
            if isinstance(child, File):
                size += child.size
            elif isinstance(child, Directory):
                size += child.total_size()
        return size
