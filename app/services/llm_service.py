import asyncio


class LLMServiceError(Exception):
    pass


async def fake_llm_call(prompt: str) -> str:
    await asyncio.sleep(1)
    return f"model-response: {prompt}"


async def get_llm_response(prompt: str) -> str:
    try:
        return await asyncio.wait_for(
            fake_llm_call(prompt),
            timeout=2
        )
    except TimeoutError as exc:
        raise LLMServiceError("LLM request timed out") from exc


async def main() -> None:
    try:
        result = await get_llm_response("hello")
        print(result)
    except LLMServiceError as exc:
        print(f"Service error: {exc}")


asyncio.run(main())