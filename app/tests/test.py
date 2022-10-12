import aiohttp
import asyncio
import pytest

# This needs pytest-asyncio plugin
@pytest.mark.asyncio
async def test_async_configmap():

    async with aiohttp.ClientSession() as session:

        minikube_url = 'http://192.168.49.2/test'
        async with session.get(minikube_url) as resp:
            text_response = await resp.text()
            # This messsage should be the one put in the configMap in k8s/configmap.yml 
            assert text_response == "<p>This is the configmap message</p>" 

asyncio.run(test_async_configmap()) 
