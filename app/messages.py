from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


def get_role(message: Message) -> str:
    return message.role

bad_message = Message(
    role=123,
    content=True
)



def get_content(message: Message) -> str:
    return message.content

def print_chat(messages: list[Message]) -> None:
    for message in messages:
        print(f"{message.role}: {message.content}")

messages: list[Message] = [
    Message(
        role="user",
        content="Explain what RAG is"
    ),
    Message(
        role="assistant",
        content="RAG combines retrieval with an LLM"
    )
]


