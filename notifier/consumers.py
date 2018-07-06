from channels.consumer import AsyncConsumer

class EchoConsumer(AsyncConsumer):

    async def websocker_connect(self, event):
        await self.send({
            "type":"webscoket.accept"
        })

    async def websocket_receive(self, event):
        #Echo the received payload
        await self.send({
            "type":"websocket.send",
            "text":event["text"],
        })
