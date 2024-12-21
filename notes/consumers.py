import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NotesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 例如: ws/notes/testRoom/
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_name = f"notes_{self.room_name}"

        # 加入 group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # 接受 WebSocket 连接
        await self.accept()

    async def disconnect(self, close_code):
        # 离开 group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # 处理前端发送的消息
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        # 将消息广播到 group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # 从 group 中接收到的事件，将其发送给 WebSocket 客户端
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))