import aiohttp
import pytest


async def logs(cont, name):
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(
            f"http://xx/containers/{cont}/logs?follow=1&stdout=1"
        ) as resp:
            async for line in resp.content:
                print(name, line)


@pytest.mark.asyncio
async def test_logs_default(capsys):
    name = "hello-world"
    container = "hello"
    await logs(container, name)
    captured = capsys.readouterr()
    assert name in captured.out and "Hello!" in captured.out


@pytest.mark.asyncio
async def test_logs_wrong_container(capsys):
    name = "hello-world"
    container = "hello1"
    await logs(container, name)
    captured = capsys.readouterr()
    assert name in captured.out and f"No such container" in captured.out


@pytest.mark.asyncio
async def test_logs_int_name(capsys):
    name = 1
    container = "hello"
    await logs(container, name)
    captured = capsys.readouterr()
    assert f"{name}" in captured.out and "Hello!" in captured.out


@pytest.mark.asyncio
async def test_logs_none_name(capsys):
    name = None
    container = "hello"
    await logs(container, name)
    captured = capsys.readouterr()
    assert f"{name}" in captured.out and "Hello!" in captured.out


@pytest.mark.asyncio
async def test_logs_empty_str_name(capsys):
    name = ""
    container = "hello"
    await logs(container, name)
    captured = capsys.readouterr()
    assert name in captured.out and "Hello!" in captured.out
