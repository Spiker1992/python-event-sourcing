from dataclasses import dataclass


@dataclass
class PostWasCreated():
    title: str
    content: str

@dataclass
class PostWasPublished():
    ...
